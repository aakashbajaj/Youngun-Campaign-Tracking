import React, { Component } from "react";

export default class StoryMetric extends Component {
  render() {
    var icon_name;
    switch (this.props.platform) {
      case "fb":
        icon_name = "facebook";
        break;
      case "in":
        icon_name = "instagram";
        break;
      case "tw":
        icon_name = "twitter";
        break;

      default:
        break;
    }
    return (
      <div className="card">
        <div className="card-body py-4">
          <div className="d-flex flex-row justify-content-center align-items">
            <i className={`mdi mdi-${icon_name} text-${icon_name} icon-lg`}></i>
            <div className="ml-3">
              <h6 className={`text-${icon_name} font-weight-semibold mb-1`}>
                {this.props.mainText}
              </h6>
              <p className="text-muted card-text">{this.props.subText}</p>
            </div>
          </div>
        </div>
      </div>
    );
  }
}
