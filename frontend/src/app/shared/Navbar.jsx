import React, { Component } from "react";
import { Dropdown } from "react-bootstrap";
import CampaignContext from "../data/CampaignContext";

class Navbar extends Component {
  static contextType = CampaignContext;

  toggleOffcanvas() {
    document.querySelector(".sidebar-offcanvas").classList.toggle("active");
  }

  onSignOutBtnClick = (evt) => {
    evt.preventDefault();
    this.context.logout(() => {
      this.props.history.push("/login");
    });
  };

  render() {
    return (
      <nav className="navbar col-lg-12 col-12 p-lg-0 fixed-top d-flex flex-row">
        <div className="navbar-menu-wrapper d-flex align-items-center justify-content-between">
          <a
            className="navbar-brand brand-logo-mini align-self-center d-lg-none"
            href="!#"
            onClick={(evt) => evt.preventDefault()}
          >
            <img
              src={require("../../assets/images/logo-mini.svg")}
              alt="logo"
            />
          </a>
          <button
            className="navbar-toggler navbar-toggler align-self-center"
            type="button"
            onClick={() => document.body.classList.toggle("sidebar-icon-only")}
          >
            <i className="mdi mdi-menu"></i>
          </button>
          <ul className="navbar-nav navbar-nav-left header-links">
            {Object.keys(this.context.campaigns).map((keyName, i) => {
              var classes = "nav-item d-none d-xl-flex nav-link";
              if (this.context.currentCampaignInView === keyName) {
                classes = classes + " active";
              }
              return (
                <li className={classes} key={keyName}>
                  <a
                    href="#"
                    onClick={this.context.setCurrentCampaign}
                    id={keyName}
                    className="nav-link"
                  >
                    <i className="mdi mdi-elevation-rise"></i>
                    {this.context.campaigns[keyName].name}
                  </a>
                </li>
              );
            })}
          </ul>
          <ul className="navbar-nav navbar-nav-right ml-lg-auto">
            <li className="nav-item  nav-profile border-0">
              <Dropdown alignRight>
                <Dropdown.Toggle className="nav-link count-indicator bg-transparent">
                  <span className="profile-text">
                    {this.context.user
                      ? this.context.user.full_name
                      : this.context.userEmail}
                  </span>
                  {/* <img
                    className="img-xs rounded-circle"
                    src={require("../../assets/images/faces/face8.jpg")}
                    alt="Profile"
                  /> */}
                </Dropdown.Toggle>
                <Dropdown.Menu className="preview-list navbar-dropdown pb-3">
                  <Dropdown.Item
                    className="dropdown-item preview-item d-flex align-items-center border-0 mt-2"
                    onClick={this.onSignOutBtnClick}
                  >
                    Sign Out
                  </Dropdown.Item>
                </Dropdown.Menu>
              </Dropdown>
            </li>
          </ul>
          <button
            className="navbar-toggler navbar-toggler-right d-lg-none align-self-center"
            type="button"
            onClick={this.toggleOffcanvas}
          >
            <span className="mdi mdi-menu"></span>
          </button>
        </div>
      </nav>
    );
  }
}

export default Navbar;
