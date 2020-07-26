import React, { Component } from "react";
import { Link, withRouter } from "react-router-dom";
import CampaignContext from "../data/CampaignContext";
// import { Collapse } from "react-bootstrap";
// import { Dropdown } from "react-bootstrap";

class Sidebar extends Component {
  static contextType = CampaignContext;
  state = {};

  toggleMenuState(menuState) {
    if (this.state[menuState]) {
      this.setState({ [menuState]: false });
    } else if (Object.keys(this.state).length === 0) {
      this.setState({ [menuState]: true });
    } else {
      Object.keys(this.state).forEach((i) => {
        this.setState({ [i]: false });
      });
      this.setState({ [menuState]: true });
    }
  }

  componentDidUpdate(prevProps) {
    if (this.props.location !== prevProps.location) {
      this.onRouteChanged();
    }
  }

  onRouteChanged() {
    document.querySelector("#sidebar").classList.remove("active");
    Object.keys(this.state).forEach((i) => {
      this.setState({ [i]: false });
    });
  }
  render() {
    return (
      <nav className="sidebar sidebar-offcanvas" id="sidebar">
        <div className="text-center sidebar-brand-wrapper d-flex align-items-center">
          {/* <a className="sidebar-brand brand-logo" href="index.html">
            <img src={require("../../assets/images/Y_logo.png")} alt="logo" />
          </a> */}
          <div className="brand-logo text-center mt-5">
            <img
              src={require("../../assets/images/youngun-logo.png")}
              alt="logo"
              style={{ width: "50%", height: "31%" }}
            />
          </div>
          <a className="sidebar-brand brand-logo-mini pt-3" href="index.html">
            <img
              src={require("../../assets/images/logo-mini.svg")}
              alt="logo"
            />
          </a>
        </div>
        <ul className="nav mt-5 pt-5">
          <li
            className={this.isPathActive("/") ? "nav-item active" : "nav-item"}
          >
            <Link className="nav-link" to="/">
              <i className="mdi mdi-television menu-icon"></i>
              <span className="menu-title">Dashboard</span>
            </Link>
          </li>

          <li
            className={
              this.isPathActive("/postsfeed") ? "nav-item active" : "nav-item"
            }
          >
            <Link className="nav-link" to="/postsfeed">
              <i className="mdi mdi-fullscreen menu-icon"></i>
              <span className="menu-title">Posts Feed</span>
            </Link>
          </li>

          <li
            className={
              this.isPathActive("/storiesfeed") ? "nav-item active" : "nav-item"
            }
          >
            <Link className="nav-link" to="/storiesfeed">
              <i className="mdi mdi-fullscreen menu-icon"></i>
              <span className="menu-title">Stories Feed</span>
            </Link>
          </li>

          {/* {this.context.campaigns[this.context.currentCampaignInView].status ===
          "completed" ? (
            <li
              className={
                this.isPathActive("/report") ? "nav-item active" : "nav-item"
              }
            >
              <Link className="nav-link" to="/report">
                <i className="mdi mdi-table-large menu-icon"></i>
                <span className="menu-title">Report</span>
              </Link>
            </li>
          ) : null} */}
        </ul>
      </nav>
    );
  }

  isPathActive(path) {
    return this.props.location.pathname.startsWith(path);
  }

  componentDidMount() {
    this.onRouteChanged();
    // add className 'hover-open' to sidebar navitem while hover in sidebar-icon-only menu
    const body = document.querySelector("body");
    document.querySelectorAll(".sidebar .nav-item").forEach((el) => {
      el.addEventListener("mouseover", function () {
        if (body.classList.contains("sidebar-icon-only")) {
          el.classList.add("hover-open");
        }
      });
      el.addEventListener("mouseout", function () {
        if (body.classList.contains("sidebar-icon-only")) {
          el.classList.remove("hover-open");
        }
      });
    });
  }
}

export default withRouter(Sidebar);
