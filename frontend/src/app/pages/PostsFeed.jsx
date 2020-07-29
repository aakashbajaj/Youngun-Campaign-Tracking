import React, { Component, lazy } from "react";
import CampaignContext from "../data/CampaignContext";
import Spinner from "../shared/Spinner";
import { Dropdown } from "react-bootstrap";

// import InstaFeed from "./InstaFeed";
// import FBFeed from "./FBFeed";
// import TwitterFeed from "./TwitterFeed";

const InstaFeed = lazy(() => import("./InstaFeed"));
const FBFeed = lazy(() => import("./FBFeed"));
const TwitterFeed = lazy(() => import("./TwitterFeed"));

export default class PostsFeed extends Component {
  static contextType = CampaignContext;

  createMarkup(embed_code) {
    return { __html: embed_code };
  }

  constructor(props) {
    super(props);

    this.state = {
      curr_platform: "in",
    };
  }

  componentDidMount() {
    console.log("in PostsFeed CDM");
    // window.fbAsyncInit();
  }

  componentDidUpdate(prevProps, prevState) {
    // window.instgrm.Embeds.process();
    // window.fbAsyncInit();
  }

  onImgLoad = (evt) => {
    evt.preventDeafult();
    // this.setState({ :  });
  };

  selectPlatform = (evt) => {
    evt.preventDefault();
    this.setState({ curr_platform: evt.target.id });
  };

  getPlatformName(id) {
    switch (id) {
      case "in":
        return "Instagram";
      case "fb":
        return "Facebook";
      case "tw":
        return "Twitter";
      default:
        return "";
    }
  }

  render() {
    return (
      <div>
        <div className="page-header">
          <Dropdown alignRight>
            <Dropdown.Toggle className="btn btn-lg btn-primary dropdown-toggle">
              {/* <i className="mdi mdi-file-outline"></i>
              <span className="count">7</span> */}
              {this.state.curr_platform === "in"
                ? "Instagram"
                : this.state.curr_platform === "fb"
                ? "Facebook"
                : "Twitter"}
            </Dropdown.Toggle>
            <Dropdown.Menu className="navbar-dropdown preview-list">
              <Dropdown.Item
                className="dropdown-item  d-flex align-items-center"
                href="!#"
                disabled
              >
                <p className="mb-0 font-weight-medium float-left">
                  Select Platform
                </p>
              </Dropdown.Item>
              <div className="dropdown-divider"></div>
              <Dropdown.Item
                className="dropdown-item preview-item d-flex align-items-center"
                href="!#"
                id="in"
                onClick={this.selectPlatform}
              >
                <div className="preview-item-content flex-grow">
                  <p
                    id="in"
                    onClick={this.selectPlatform}
                    className="preview-subject ellipsis font-weight-medium text-dark"
                  >
                    <i
                      id="in"
                      onClick={this.selectPlatform}
                      className={
                        "mdi mdi-instagram text-instagram icon-sm mr-2"
                      }
                    ></i>{" "}
                    Instagram{" "}
                  </p>
                </div>
              </Dropdown.Item>
              <div className="dropdown-divider"></div>
              <Dropdown.Item
                className="dropdown-item preview-item d-flex align-items-center"
                href="!#"
                id="fb"
                onClick={this.selectPlatform}
              >
                <div className="preview-item-content flex-grow">
                  <p
                    id="fb"
                    onClick={this.selectPlatform}
                    className="preview-subject ellipsis font-weight-medium text-dark"
                  >
                    <i
                      id="fb"
                      onClick={this.selectPlatform}
                      className={"mdi mdi-facebook text-facebook icon-sm mr-2"}
                    ></i>{" "}
                    Facebook{" "}
                  </p>
                </div>
              </Dropdown.Item>
              <div className="dropdown-divider"></div>
              <Dropdown.Item
                className="dropdown-item preview-item d-flex align-items-center"
                href="!#"
                id="tw"
                onClick={this.selectPlatform}
              >
                <div className="preview-item-content flex-grow">
                  <p
                    id="tw"
                    onClick={this.selectPlatform}
                    className="preview-subject ellipsis font-weight-medium text-dark"
                  >
                    <i
                      id="fb"
                      onClick={this.selectPlatform}
                      className={"mdi mdi-twitter text-twitter icon-sm mr-2"}
                    ></i>{" "}
                    Twitter{" "}
                  </p>
                </div>
              </Dropdown.Item>
            </Dropdown.Menu>
          </Dropdown>
          <h3 className="page-title">Posts</h3>
        </div>
        {this.state.curr_platform === "in" ? (
          <InstaFeed />
        ) : this.state.curr_platform === "fb" ? (
          <FBFeed />
        ) : (
          <TwitterFeed />
        )}
      </div>
    );
  }
}
