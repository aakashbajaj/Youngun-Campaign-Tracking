import React, { Component } from "react";
import { Form, Button } from "react-bootstrap";

export class VerifyOtp extends Component {
  state = {
    email: "abcd@email.com",
    otptoken: "",
  };

  onChangeHandler = (evt) => {
    evt.preventDefault();
    this.setState({ [evt.target.id]: evt.target.value });
  };

  onSignInBtnClick = (evt) => {
    evt.preventDefault();
  };

  render() {
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
                <Form className="pt-3" onSubmit={this.onSignInBtnClick}>
                  <Form.Group className="d-flex search-field">
                    <Form.Control
                      id="email"
                      type="email"
                      placeholder="Email"
                      size="lg"
                      className="h-auto text-muted"
                      value={this.state.email}
                      onChange={this.onChangeHandler}
                      disabled
                    />
                  </Form.Group>
                  <Form.Group className="d-flex search-field">
                    <Form.Control
                      type="otptoken"
                      placeholder="OTP"
                      size="lg"
                      className="h-auto"
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
                  <div className="my-2 d-flex justify-content-between align-items-center">
                    <div className="form-check">
                      <label className="form-check-label text-muted">
                        <input type="checkbox" className="form-check-input" />
                        <i className="input-helper"></i>
                        Keep me signed in
                      </label>
                    </div>
                  </div>
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
