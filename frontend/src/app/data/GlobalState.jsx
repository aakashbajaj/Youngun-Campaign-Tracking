import React, { Component } from "react";
import API, { setAuthTokenHeader } from "../utils/api";
import CampaignContext from "./CampaignContext";

export default class GlobalState extends Component {
  state = {
    user: null,
    userEmail: null,
    isAuthenticated: false,
    isAuthInProgress: false,
    sendingOTP: false,
    errors: [],
    campaigns: {},
    liveCampaignData: {},
    liveCampaignFeed: {},
    campaignReportData: {},
    currentCampaignInView: null,
  };

  // constructor(props) {
  //   super(props);
  // }

  componentDidMount() {
    this.loadTempCredentials();
  }
  //#region fetchData
  async fetchAllData() {
    const userInfo = await API.get("/api/users/");
    console.log(userInfo.data);
    this.setState({ user: userInfo.data.user });

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
  //#endregion

  //#region Event Handler
  setCurrentCampaign = (evt) => {
    console.log(evt.target.id);
    this.setState({ currentCampaignInView: evt.target.id });
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
    this.fetchAllData();
  }
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
      localStorage.setItem("campaigntoken", resp.data["token"]);
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
      // var errors = err.response.data["non_field_errors"];
      // this.setState({ errors: err.response });
    }
  };

  logout(cb) {
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
    };

    //delete token from LS
    setAuthTokenHeader(null);
    localStorage.removeItem("campaigntoken");

    this.setState({ state: newState });

    cb();
  }
  //#endregion

  function_collection = {
    login: this.login,
    logout: this.logout,
    verify: this.verify,
    setCurrentCampaign: this.setCurrentCampaign,
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