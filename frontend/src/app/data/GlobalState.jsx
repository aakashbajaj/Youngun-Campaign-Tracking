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
    campaigns: [],
    liveCampaignData: {},
    liveCampaignFeed: {},
    campaignReportData: {},
    currentCampaignInVIew: null,
  };

  componentDidMount() {}

  async fetchAllData() {
    const resp = await API.get("/api/campaigns/");

    console.log(resp);
  }

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
      currentCampaignInVIew: null,
    };

    //delete token from LS
    setAuthTokenHeader(null);
    localStorage.removeItem("campaigntoken");

    this.setState({ state: newState });

    cb();
  }

  render() {
    return (
      <CampaignContext.Provider
        value={{
          ...this.state,
          login: this.login,
          logout: this.logout,
          verify: this.verify,
        }}
      >
        {this.props.children}
      </CampaignContext.Provider>
    );
  }
}
