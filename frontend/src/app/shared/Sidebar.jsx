import React, { Component } from "react";
import { Link, withRouter } from "react-router-dom";
import CampaignContext from "../data/CampaignContext";
import { Collapse } from "react-bootstrap";
import { Dropdown } from "react-bootstrap";
import Spinner from "./Spinner";
import "./Sidebar.css";

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

    const dropdownPaths = [
      { path: "/dashboard", state: "dashboardMenuOpen" },
      { path: "/posts-feed", state: "postsFeedMenuOpen" },
      { path: "/tables", state: "tablesMenuOpen" },
      { path: "/icons", state: "iconsMenuOpen" },
      { path: "/charts", state: "chartsMenuOpen" },
      { path: "/report", state: "reportPageMenuOpen" },
    ];

    dropdownPaths.forEach((obj) => {
      if (this.isPathActive(obj.path)) {
        this.setState({ [obj.state]: true });
      }
    });
  }
  render() {
    // if (this.context.currentCampaignInView != null) {
    //   return <Spinner />;
    // }

    var showReport = false;

    var currCampName = null;

    var showStories = false;

    if (this.context.currentCampaignInView) {
      // console.log("Changing " + this.context.currentCampaignInView);
      currCampName = this.context.currentCampaignInView;
    }

    var currentCampaignInView = this.context.currentCampaignInView;

    if (currentCampaignInView) {
      if (this.context.campaigns[currentCampaignInView]) {
        if (
          this.context.campaigns[currentCampaignInView].campaign_module === "v2"
        ) {
          showReport = true;
        }

        if (this.context.liveCampaignData[currentCampaignInView]) {
          if (
            this.context.liveCampaignData[currentCampaignInView]
              .live_stories_cnt > 0
          )
            showStories = true;
          // console.log(showStories);
        }
      }
    }

    // if (!currentCampaignInView) {
    //   return <Spinner />;
    // }

    return (
      <nav className="sidebar sidebar-offcanvas" id="sidebar">
        <div className="text-center sidebar-brand-wrapper d-flex align-items-center">
          {/* <a className="sidebar-brand brand-logo" href="index.html">
            <img src={require("../../assets/images/Y_logo.png")} alt="logo" />
          </a> */}
          <div className="brand-logo text-center mt-5">
            <img
              src={require("../../assets/images/youngunnew.jpg")}
              alt="logo"
              style={{ width: "80%", height: "61%" }}
            />
          </div>
          <a className="sidebar-brand brand-logo-mini pt-3" href="index.html">
            <img
              src={require("../../assets/images/youngunnew.jpg")}
              alt="logo"
            />
          </a>
        </div>
        <ul className="nav mt-5 pt-5">
          {currCampName === null ? (
            <li className="nav-item d-xl-flex nav-link">
              <Dropdown alignRight>
                <Dropdown.Toggle className="nav-link count-indicator bg-transparent">
                  <span className="profile-text">Loading....</span>
                </Dropdown.Toggle>
              </Dropdown>
            </li>
          ) : (
            <li className="nav-item d-xl-flex nav-link">
              <Dropdown alignRight>
                <Dropdown.Toggle className="nav-link bg-transparent dropdown-toggle">
                  <span>
                    <i className="mdi mdi-elevation-rise"></i>
                    {this.context.campaigns[currCampName].name}
                  </span>
                </Dropdown.Toggle>
                <Dropdown.Menu className="preview-list navbar-dropdown pb-3">
                  {Object.keys(this.context.campaigns).map((keyName, i) => {
                    return (
                      <Dropdown.Item
                        className="dropdown-item preview-item d-flex align-items-center border-0 mt-2"
                        key={keyName}
                        id={keyName}
                        onClick={this.context.setCurrentCampaign}
                      >
                        <i className="mdi mdi-elevation-rise"></i>
                        {this.context.campaigns[keyName].name}
                      </Dropdown.Item>
                    );
                  })}
                </Dropdown.Menu>
              </Dropdown>
            </li>
          )}
          <li
            className={this.isPathActive("/") ? "nav-item active activetab" : "nav-item"}
          >
            <Link className="nav-link" to="/">
              <i className="mdi mdi-television menu-icon"></i>
              <span className="menu-title">Dashboard</span>
            </Link>
          </li>

          <li
            className={
              this.isPathActive("/postsfeed") ? "nav-item active activetab" : "nav-item"
            }
          >
            <Link className="nav-link" to="/postsfeed">
              <i className="mdi mdi-image menu-icon"></i>
              <span className="menu-title">Posts Feed</span>
            </Link>
          </li>
          {showStories ? (
            <li
              className={
                this.isPathActive("/storiesfeed")
                  ? "nav-item active activetab"
                  : "nav-item"
              }
            >
              <Link className="nav-link" to="/storiesfeed">
                <i className="mdi mdi-history menu-icon"></i>
                <span className="menu-title">Stories Feed</span>
              </Link>
            </li>
          ) : null}

          {/* <li
            className={
              this.isPathActive("/report") ? "nav-item active activetab" : "nav-item"
            }
          >
            <Link className="nav-link" to="/report">
              <i className="mdi mdi-fullscreen menu-icon"></i>
              <span className="menu-title">Reporting</span>
            </Link>
          </li> */}

          {showReport ? (
            <li
              className={
                this.isPathActive("/report/post-stats")
                  ? "nav-item active activetab"
                  : "nav-item"
              }
            >
              <Link className="nav-link" to="/report/post-stats">
                <i className="mdi mdi-history menu-icon"></i>
                <span className="menu-title">Post Statistics</span>
              </Link>
            </li>
          ) : // <li
          //   className={
          //     this.isPathActive("/report") ? "nav-item active activetab" : "nav-item"
          //   }
          // >
          //   <div
          //     className={
          //       this.state.reportPageMenuOpen
          //         ? "nav-link menu-expanded"
          //         : "nav-link"
          //     }
          //     onClick={() => this.toggleMenuState("reportPageMenuOpen")}
          //     data-toggle="collapse"
          //   >
          //     <i className="mdi mdi-table-large menu-icon"></i>
          //     <span className="menu-title">Reporting</span>
          //     <i className="menu-arrow"></i>
          //   </div>
          //   <Collapse in={this.state.reportPageMenuOpen}>
          //     <ul className="nav flex-column sub-menu">
          //       <li className="nav-item">
          //         {" "}
          //         <Link
          //           className={
          //             this.isPathActive("/report/post-stats")
          //               ? "nav-link active"
          //               : "nav-link"
          //           }
          //           to="/report/post-stats"
          //         >
          //           Post Statistics
          //         </Link>
          //       </li>

          //       <li className="nav-item">
          //         {" "}
          //         <Link
          //           className={
          //             this.isPathActive("/report/overview")
          //               ? "nav-link active"
          //               : "nav-link"
          //           }
          //           to="/report/overview"
          //         >
          //           Campaign Overview
          //         </Link>
          //       </li>
          //     </ul>
          //   </Collapse>
          // </li>
          null}
        </ul>
      </nav>
    );
  }

  isPathActive(path) {
    // console.log(path);
    // console.log(this.props.location.pathname);
    return this.props.location.pathname.endsWith(path);
  }

  componentDidMount() {
    this.onRouteChanged();
    // add className 'hover-open' to sidebar navitem while hover in sidebar-icon-only menu
    const body = document.querySelector("body");
    document.querySelectorAll(".sidebar .nav-item").forEach((el) => {
      el.addEventListener("mouseover", function () {
        // console.log(el);
        // console.log(body);
        // console.log(body.classList);
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
