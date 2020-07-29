import React, { Component } from "react";
import API, { setAuthTokenHeader } from "../utils/api";
import CampaignContext from "./CampaignContext";
import Cookie from "js-cookie";

import Notify from "../utils/notify";

export default class GlobalState extends Component {
  state = {
    user: null,
    userEmail: null,
    isAuthenticated: false,
    isAuthInProgress: false,
    sendingOTP: false,
    errors: {},
    campaigns: {},
    liveCampaignData: {},
    liveCampaignFeed: {},
    campaignReportData: {},
    currentCampaignInView: null,
    invited_profiles: {},
    maskedData: null,
  };

  // constructor(props) {
  //   super(props);
  // }

  componentDidMount() {
    // this.loadTempCredentials();
    this.loadTokenFromCookie();
  }

  //#region fetchData
  async fetchAllData() {
    try {
      const userInfo = await API.get("/api/profile/");
      console.log(userInfo.data);
      this.setState({ user: userInfo.data.profile });
    } catch (error) {
      console.log(error.response);
    }

    this.getInvitedUsersData();

    const resp = await API.get("/api/campaigns/");

    console.log(resp.data.campaigns);
    const campaigns = resp.data.campaigns;
    var campData = {};
    var firstCampaign = null;

    campaigns.forEach((campaign) => {
      campData[campaign.slug] = campaign;
      if (firstCampaign === null) firstCampaign = campaign.slug;

      API.get(`/api/campaigns/${campaign.slug}/metrics`)
        .then((resp) => {
          console.log(resp.data);
          this.addLiveCampaignData(campaign.slug, resp.data.campaign);
        })
        .catch((err) => {
          console.log(err.response);
        });

      API.get(`/api/campaigns/${campaign.slug}/feed`)
        .then((resp) => {
          console.log(resp.data);
          this.addLiveCampaignFeed(campaign.slug, resp.data.campaign);
        })
        .catch((err) => {
          console.log(err.response);
        });
    });

    this.setState({
      campaigns: campData,
      currentCampaignInView: firstCampaign,
    });
  }

  addLiveCampaignData(slug, data) {
    const newLiveCampData = {
      ...this.state.liveCampaignData,
      [slug]: data,
    };
    const newState = {
      ...this.state,
      liveCampaignData: newLiveCampData,
    };
    this.setState(newState);
  }

  addLiveCampaignFeed(slug, data) {
    const newLiveCampFeed = {
      ...this.state.liveCampaignFeed,
      [slug]: data,
    };
    const newState = {
      ...this.state,
      liveCampaignFeed: newLiveCampFeed,
    };
    this.setState(newState);
  }

  getInvitedUsersData = () => {
    API.get("/api/profile/myinvites/")
      .then((resp) => {
        console.log(resp.data);
        this.setState({ invited_profiles: resp.data.invited_profile });
      })
      .catch((err) => {
        console.log(err.response);
      });
  };
  //#endregion

  //#region Event Handler
  setCurrentCampaign = (evt) => {
    console.log(evt.target.id);
    this.setState({ currentCampaignInView: evt.target.id });
  };
  //#endregion

  //#region Actions
  inviteEmailUser = (email, cb) => {
    const data = {
      email: email,
      campaign_slug: this.state.currentCampaignInView,
    };
    API.post("/api/profile/inviteuser/", data)
      .then((resp) => {
        console.log(resp.data);
        this.getInvitedUsersData();
      })
      .catch((err) => {
        console.log(err.response);
      });
    cb();
  };

  removeInvitedUser = (email) => {
    const data = {
      email: email,
      campaign_slug: this.state.currentCampaignInView,
    };
    API.post("/api/profile/removeinvite/", data)
      .then((resp) => {
        console.log(resp.data);
        this.getInvitedUsersData();
      })
      .catch((err) => {
        console.log(err.response);
      });
  };
  //#endregion
  //#region utility functions
  loadTempCredentials() {
    const token = "07b833d53b38f85517dcb922b94e1a7ff841c950";
    const userEmail = "aakashbajaj2007@gmail.com";

    setAuthTokenHeader(token);
    const newState = {
      ...this.state,
      userEmail: userEmail,
      user: {
        email: userEmail,
        token: token,
      },
      isAuthenticated: true,
    };

    this.setState(newState);
    this.authenticate();
  }

  loadTokenFromCookie() {
    const token = Cookie.get("djangotoken") ? Cookie.get("djangotoken") : null;
    if (token) {
      setAuthTokenHeader(token);
      const newState = {
        ...this.state,
        user: {
          email: "",
          token: token,
        },
        isAuthenticated: true,
      };

      this.setState(newState, this.authenticate);
    }
  }

  resetToken() {
    Cookie.remove("djangotoken");
  }

  authenticate() {
    this.fetchAllData();
  }

  deauthenticate() {
    this.logout();
  }

  initiateLogin = async (email, cb) => {
    try {
      const data = {
        email: email,
      };

      const newState = {
        ...this.state,
        userEmail: email,
        isAuthenticated: false,
        isAuthInProgress: true,
        sendingOTP: true,
        maskedData: null,
      };
      this.setState(newState);

      var resp = await API.post("/api/users/login/", data);
      console.log(resp.data);

      this.setState({ maskedData: resp.data });
      cb();
    } catch (err) {
      console.log("ERROR");
      console.log(err.response);
      // window.alert(err.response);

      Notify.notifyError(err.response.data.response);
      const newState = {
        ...this.state,
        userEmail: email,
        isAuthenticated: false,
        isAuthInProgress: false,
        sendingOTP: false,
      };
      this.setState(newState);
    }
  };

  verifyOTPToken = async (otptoken, cb) => {
    try {
      console.log(this.state);

      const data = {
        tempid: this.state.maskedData.tempid,
        inpotp: otptoken,
      };
      this.setState({ sendingOTP: false });

      const resp = await API.post("/api/users/verify/", data);
      console.log(resp);
      console.log(resp.data["token"]);
      // set token in localStorage
      // localStorage.setItem("campaigntoken", resp.data["token"]);
      Cookie.set("djangotoken", resp.data["token"], { expires: 1 });
      setAuthTokenHeader(resp.data["token"]);

      // setting authenticated user field in global state
      const newState = {
        ...this.state,
        user: {
          email: this.state.userEmail,
          token: resp.data["token"],
        },
        isAuthenticated: true,
        isAuthInProgress: false,
        maskedData: null,
      };
      this.setState(newState);
      this.authenticate();
      cb();
    } catch (err) {
      console.log("ERROR");
      console.log(err.response);
      // window.alert(err.response);

      Notify.notifyError(err.response.data.response);
      const newState = {
        ...this.state,
        userEmail: this.state.userEmail,
        isAuthenticated: false,
        isAuthInProgress: false,
        sendingOTP: false,
      };
      this.setState(newState);
    }
  };
  //#endregion

  //#region user login, logout
  login = async (email, cb) => {
    try {
      var formData = new FormData();
      formData.append("email", email);

      const newState = {
        ...this.state,
        userEmail: email,
        isAuthenticated: false,
        isAuthInProgress: true,
        sendingOTP: true,
      };
      this.setState(newState);

      console.log(formData);
      const resp = await API.post("/otpauth/email/", formData);

      console.log(resp);

      cb();
    } catch (err) {
      console.log("ERROR");
      console.log(err.response);
      window.alert(err.response);

      const newState = {
        ...this.state,
        userEmail: email,
        isAuthenticated: false,
        isAuthInProgress: false,
        sendingOTP: false,
      };
      this.setState(newState);
      // var errors = err.response.data["non_field_errors"];
      // this.setState({ errors: errors });
    }
  };

  verify = async (otptoken, cb) => {
    try {
      console.log(this.state);

      var formData = new FormData();
      formData.append("email", this.state.userEmail);
      formData.append("token", otptoken);
      this.setState({ sendingOTP: false });

      const resp = await API.post("/otpauth/token/", formData);
      console.log(resp);
      console.log(resp.data["token"]);
      // set token in localStorage
      // localStorage.setItem("campaigntoken", resp.data["token"]);
      Cookie.set("djangotoken", resp.data["token"], { expires: 1 });
      setAuthTokenHeader(resp.data["token"]);

      // setting authenticated user field in global state
      const newState = {
        ...this.state,
        user: {
          email: this.state.userEmail,
          token: resp.data["token"],
        },
        isAuthenticated: true,
        isAuthInProgress: false,
      };
      this.setState(newState);
      this.fetchAllData();
      cb();
    } catch (err) {
      console.log("ERROR");
      console.log(err.response);
      Notify.notifyError(err.response.data.token[0]);
      // var errors = err.response.data["non_field_errors"];
      // this.setState({ errors: err.response });
    }
  };

  logout = () => {
    const newState = {
      user: null,
      userEmail: null,
      isAuthenticated: false,
      isAuthInProgress: false,
      errors: [],
      campaigns: [],
      liveCampaignData: {},
      liveCampaignFeed: {},
      campaignReportData: {},
      currentCampaignInView: null,
      invited_profiles: {},
    };

    //delete token from LS
    setAuthTokenHeader(null);
    Cookie.remove("djangotoken");
    // localStorage.removeItem("campaigntoken");

    this.setState(newState);
  };
  //#endregion

  function_collection = {
    login: this.login,
    logout: this.logout,
    verify: this.verify,
    setCurrentCampaign: this.setCurrentCampaign,

    inviteEmailUser: this.inviteEmailUser,
    removeInvitedUser: this.removeInvitedUser,

    initiateLogin: this.initiateLogin,
    verifyOTPToken: this.verifyOTPToken,
  };

  render() {
    return (
      <CampaignContext.Provider
        value={{
          ...this.state,
          ...this.function_collection,
        }}
      >
        {this.props.children}
      </CampaignContext.Provider>
    );
  }
}
