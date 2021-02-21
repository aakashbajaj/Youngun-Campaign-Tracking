import React, { Component } from "react";
import { Form, Button } from "react-bootstrap";
import { Redirect } from "react-router-dom";

import CampaignContext from "../../data/CampaignContext";

export class VerifyOtp extends Component {
  static contextType = CampaignContext;

  state = {
    email: "",
    otptoken: "",
  };

  componentDidMount() {
    this.setState({ email: this.context.userEmail });
  }

  onChangeHandler = (evt) => {
    evt.preventDefault();
    this.setState({ [evt.target.id]: evt.target.value });
  };

  onSignInBtnClick = (evt) => {
    evt.preventDefault();
    this.context.verifyOTPToken(this.state.otptoken, () => {
      this.props.history.push("/");
    });
  };

  render() {
    if (!this.context.isAuthInProgress && !this.context.isAuthenticated) {
      return <Redirect to="/login" />;
    }
    return (
      <div>
        <div className="d-flex align-items-center auth px-0">
          <div className="row w-100 mx-0">
            <div className="col-lg-4 mx-auto">
              <div className="auth-form-light text-left py-5 px-4 px-sm-5">
                <div className="brand-logo text-center">
                  <img
                    src={require("../../../assets/images/youngunnew.jpg")}
                    alt="logo"
                    style={{ width: "80%", height: "61%" }}
                  />
                </div>
                {/* {this.context.maskedData ? (
                  <h6 className="font-weight-light">
                    OTP has been sent to {this.context.maskedData.masked_email}
                    {this.context.maskedData.masked_mobile
                      ? " and " + this.context.maskedData.masked_mobile
                      : null}
                  </h6>
                ) : null} */}
                <h4>Enter the OTP to continue</h4>
                <Form className="pt-3" onSubmit={this.onSignInBtnClick}>
                  <Form.Group className="d-flex search-field">
                    <Form.Control
                      id="email"
                      type="email"
                      placeholder="Email"
                      size="lg"
                      className="h-auto text-muted"
                      style ={{
                        backgroundColor: "white"
                      }}
                      value={this.state.email}
                      onChange={this.onChangeHandler}
                      disabled
                    />
                  </Form.Group>
                  <Form.Group className="d-flex search-field">
                    <Form.Control
                      id="otptoken"
                      type="password"
                      placeholder="OTP"
                      size="lg"
                      className="h-auto"
                      style ={{
                        backgroundColor: "white"
                      }}
                      value={this.state.otptoken}
                      onChange={this.onChangeHandler}
                    />
                  </Form.Group>

                  <div className="mt-3">
                    <Button
                      className="btn btn-block btn-primary btn-lg font-weight-medium auth-form-btn"
                      type="submit"
                    >
                      LOGIN
                    </Button>
                  </div>
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

export default VerifyOtp;
