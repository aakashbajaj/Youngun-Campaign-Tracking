import React, { Component } from "react";
import { Form, Button } from "react-bootstrap";
import { Redirect } from "react-router-dom";

import CampaignContext from "../data/CampaignContext";

export class Login extends Component {
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
    if (!this.context.isAuthInProgress && this.context.isAuthenticated) {
      return <Redirect to="/" />;
    }
    return (
      <div>
        <div className="d-flex align-items-center auth px-0">
          <div className="row w-100 mx-0">
            <div className="col-lg-4 mx-auto">
              <div className="auth-form-light text-left py-5 px-4 px-sm-5">
                <div className="brand-logo text-center">
                  <img
                    src={require("../../assets/images/youngun-logo.png")}
                    alt="logo"
                  />
                </div>
                <h4>Hello! let's get started</h4>
                <h6 className="font-weight-light">Sign in to continue.</h6>
                <Form className="pt-3" onSubmit={this.onSendOTPBtnClick}>
                  <Form.Group className="d-flex search-field">
                    <Form.Control
                      id="email"
                      type="email"
                      placeholder="Email"
                      size="lg"
                      className="h-auto"
                      value={this.state.email}
                      onChange={this.onChangeHandler}
                    />
                  </Form.Group>
                  {this.context.sendingOTP ? (
                    <h7 className="font-weight-light">Sending OTP....</h7>
                  ) : null}

                  <div className="mt-3">
                    <Button
                      className="btn btn-block btn-primary btn-lg font-weight-medium auth-form-btn"
                      type="submit"
                    >
                      SEND OTP
                    </Button>
                  </div>
                  <div className="my-2 d-flex justify-content-between align-items-center"></div>
                  {/* <div className="my-2 d-flex justify-content-between align-items-center">
                    <div className="form-check">
                      <label className="form-check-label text-muted">
                        <input type="checkbox" className="form-check-input" />
                        <i className="input-helper"></i>
                        Keep me signed in
                      </label>
                    </div>
                  </div> */}
                </Form>
              </div>
            </div>
          </div>
        </div>
      </div>
    );
  }
}

export default Login;
