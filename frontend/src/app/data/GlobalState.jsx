import React, { Component } from "react";
import API from "../utils/api";
import CampaignContext from "./CampaignContext";

export default class GlobalState extends Component {
  state = {
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

  componentDidMount() {}

  login = async (email, cb) => {
    try {
      var formData = new FormData();
      formData.append("email", email);

      const newState = {
        ...this.state,
        userEmail: email,
        isAuthenticated: false,
        isAuthInProgress: true,
      };
      this.setState(newState);

      console.log(formData);
      const resp = await API.agent.post("/otpauth/email/", formData);

      console.log(resp);

      cb();
    } catch (err) {
      console.log("ERROR");
      console.log(err.response);
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

      const resp = await API.agent.post("/otpauth/token/", formData);
      console.log(resp);
      // set token in localStorage
      localStorage.setItem("campaigntoken", resp.data["token"]);

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
    localStorage.removeItem("campaigntoken");

    this.setState({ state: newState });

    cb();
  }

  isAuthInProgress() {
    return this.state.isAuthInProgress;
  }

  isAuthenticated() {
    return this.state.isAuthenticated;
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
