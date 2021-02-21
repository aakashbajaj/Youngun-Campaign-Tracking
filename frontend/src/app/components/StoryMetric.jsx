import React, { Component } from "react";

export default class StoryMetric extends Component {
  render() {
    var icon_name;
    var extra_class;
    switch (this.props.platform) {
      case "fb":
        icon_name = "facebook";
        extra_class = "mt-2";
        break;
      case "in":
        icon_name = "instagram";
        break;
      case "tw":
        icon_name = "twitter";
        extra_class = "mt-2";
        break;

      default:
        break;
    }
    return (
      <div className="card">
        <div className="card-body py-4">
          <div className="d-flex flex-row justify-content-center align-items">
            <i
              className={`mdi mdi-${icon_name} text-${icon_name} icon-lg ${extra_class}`}
            ></i>
            <div className="ml-4">
              <h6
                className={`text-${icon_name} font-weight-semibold mb-1 mt-3`}
              >
                {this.props.PostMainText}
              </h6>
              {/* <p className="text-muted card-text">{this.props.PostSubText}</p> */}
              {this.props.StoryMainText !== "Stories Live: --" ? (
                <h6
                  className={`text-${icon_name} font-weight-semibold mb-1 mt-2`}
                >
                  {this.props.StoryMainText}
                </h6>
              ) : null}

              {/* <p className="text-muted card-text">{this.props.StorySubText}</p> */}
            </div>
            {/* <div className="ml-2"></div> */}
          </div>
        </div>
      </div>
    );
  }
}
