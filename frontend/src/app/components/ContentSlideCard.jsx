import React, { Component } from "react";

export default class ContentSlideCard extends Component {
  render() {
    return (
      <div className="card card-statistics">
        <div className="card-body">
          <div className="clearfix">
            <div className="float-left">
              <i className="mdi mdi-receipt text-warning icon-lg"></i>
            </div>
            <div className="float-right">
              <p className="mb-0 text-right text-dark"></p>
              <div className="fluid-container">
                <h3 className="font-weight-medium text-right mb-0 mt-3 text-dark">
                  <a
                    href={`${this.props.slide_url}`}
                    target="_blank"
                    rel="noopener noreferrer"
                  >
                    View Content Slide
                  </a>
                </h3>
              </div>
            </div>
          </div>
        </div>
      </div>
    );
  }
}
