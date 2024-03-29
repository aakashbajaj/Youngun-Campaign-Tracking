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
    campaignCount: 0,
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
      // console.log(userInfo.data);
      this.setState({ user: userInfo.data.profile });
    } catch (error) {
      console.log(error.response);
    }

    this.getInvitedUsersData();

    const resp = await API.get("/api/campaigns/");

    // console.log(resp.data.campaigns);
    const campaigns = resp.data.campaigns;
    var campData = {};
    var firstCampaign = null;

    if (campaigns && campaigns.length > 0) {
      this.setState({ campaignCount: campaigns.length });
      campaigns.forEach((campaign) => {
        campData[campaign.slug] = campaign;
        if (firstCampaign === null) firstCampaign = campaign.slug;

        API.get(`/api/campaigns/${campaign.slug}/metrics`)
          .then((resp) => {
            // console.log("Metrics Data:");
            // console.log(resp.data);
            this.addLiveCampaignData(campaign.slug, resp.data.campaign);
          })
          .catch((err) => {
            console.log(err.response);
          });

        API.get(`/api/campaigns/${campaign.slug}/feed`)
          .then((resp) => {
            // console.log("Feed Data:");
            // console.log(resp.data);
            this.addLiveCampaignFeed(campaign.slug, resp.data.campaign);
          })
          .catch((err) => {
            console.log(err.response);
          });

        API.get(`/api/campaigns/${campaign.slug}/report`)
          .then((resp) => {
            // console.log("Report Data:");
            // console.log(resp.data);
            this.addCampaignReportData(campaign.slug, resp.data.campaign);
          })
          .catch((err) => {
            console.log(err.response);
          });
      });

      this.setState({
        campaigns: campData,
        currentCampaignInView: firstCampaign,
      });
    } else {
      this.setState({ campaignCount: 0 });
    }
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

  sortFeedList(feedList, direction = 1) {
    return feedList.sort(function (a, b) {
      if (a.upload_date === b.upload_date) {
        return direction * (b.id < a.id ? -1 : 1);
      } else {
        return direction * (new Date(b.upload_date) < new Date(a.upload_date) ? -1 : 1);
      }
    });
  }

  addLiveCampaignFeed(slug, data) {
    // data.in_posts = this.sortFeedList(data.in_posts);
    // data.fb_posts = this.sortFeedList(data.fb_posts);
    // data.tw_posts = this.sortFeedList(data.tw_posts);

    data.instagram = this.sortFeedList(data.instagram);
    data.facebook = this.sortFeedList(data.facebook);
    data.twitter = this.sortFeedList(data.twitter);

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

  addCampaignReportData(slug, data) {
    data.posts = this.sortFeedList(data.posts, -1);

    const newCampaignReportData = {
      ...this.state.campaignReportData,
      [slug]: data,
    };
    const newState = {
      ...this.state,
      campaignReportData: newCampaignReportData,
    };
    this.setState(newState);
  }

  getInvitedUsersData = () => {
    API.get("/api/profile/myinvites/")
      .then((resp) => {
        // console.log(resp.data);
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
        // console.log(resp.data);
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

    this.authenticate(token);
  }

  loadTokenFromCookie() {
    const token = Cookie.get("djangotoken") ? Cookie.get("djangotoken") : null;
    if (token) {
      this.authenticate(token);
    }
  }

  resetToken() {
    Cookie.remove("djangotoken");
  }

  authenticate = async (token) => {
    try {
      setAuthTokenHeader(token);
      await API.get("/api/users/authenticate/");

      // set token in localStorage
      // localStorage.setItem("campaigntoken", resp.data["token"]);
      Cookie.set("djangotoken", token, { expires: 1 });

      // setting authenticated user field in global state
      const newState = {
        ...this.state,
        user: {
          email: this.state.userEmail,
          token: token,
        },
        isAuthenticated: true,
        isAuthInProgress: false,
        maskedData: null,
      };
      this.setState(newState);
      this.fetchAllData();
    } catch (err) {
      this.logout();
      Notify.notifyError("Error in Authentication");
    }
  };

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
      // console.log(resp.data);

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
      // console.log(this.state);

      const data = {
        tempid: this.state.maskedData.tempid,
        inpotp: otptoken,
      };
      this.setState({ sendingOTP: false });

      const resp = await API.post("/api/users/verify/", data);
      // console.log(resp);
      // console.log(resp.data["token"]);

      this.authenticate(resp.data["token"]);
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

      // console.log(formData);
      const resp = await API.post("/otpauth/email/", formData);

      // console.log(resp);

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
      // console.log(this.state);

      var formData = new FormData();
      formData.append("email", this.state.userEmail);
      formData.append("token", otptoken);
      this.setState({ sendingOTP: false });

      const resp = await API.post("/otpauth/token/", formData);
      // console.log(resp);
      // console.log(resp.data["token"]);
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
