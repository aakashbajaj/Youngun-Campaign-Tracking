import React, { Component } from "react";
import { Form, Button } from "react-bootstrap";
import CampaignContext from "../data/CampaignContext";
import Login from "./Login";
import VerifyOtp from "./VerifyOtp";

export class UserPage extends Component {
  static contextType = CampaignContext;

  state = {
    email: "",
  };

  onChangeHandler = (evt) => {
    evt.preventDefault();
    this.setState({ [evt.target.id]: evt.target.value });
  };

  onSendOTPBtnClick = (evt) => {
    evt.preventDefault();
    const { email } = this.state;
    console.log(email);
    this.context.login(email, () => {
      this.props.history.push("/verify");
    });
  };

  render() {
    return (
      <div>
        <div className="d-flex align-items-center auth px-0">
          <div className="row w-100 mx-0">
            <div className="col-lg-4 mx-auto">
              <div className="auth-form-light text-left py-5 px-4 px-sm-5"></div>
            </div>
          </div>
        </div>
      </div>
    );
  }
}

export default UserPage;
