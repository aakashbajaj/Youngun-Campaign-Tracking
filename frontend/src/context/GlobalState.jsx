import React, { Component } from "react";
import API from "../utility/api";

export default class GlobalState extends Component {
  state = {
    user: null,
    authDetails: null,
    isAuthenticated: false,
    isAuthInProgress: false,
    errors: [],
    campaigns: [],
    liveCampaignData: {},
    campaignReportData: {},
  };
  login = async (email, cb) => {
    try {
      var formData = new FormData();
      formData.append("email", email);
      console.log(formData);

      const newState = {
        ...this.state,
        authDetails: {
          email: email,
        },
        isAuthenticated: false,
        isAuthInProgress: true,
      };
      this.setState(newState);

      const resp = await API.post("/otpauth/email/", formData);

      console.log(resp);
      console.log("Aage chalo");

      cb();
    } catch (err) {
      console.log("ERROR");
      console.log(err.response);
      var errors = err.response.data["non_field_errors"];
      this.setState({ errors: errors });
      console.log(err);
    }
  };

  render() {
    return <div></div>;
  }
}
