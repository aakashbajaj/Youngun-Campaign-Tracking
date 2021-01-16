import React, { Component } from "react";
import { Link, withRouter } from "react-router-dom";

class ContentSlideCard extends Component {
  render() {
    return (
      <div className="card card-statistics">
        <div className="card-body">
          <div className="clearfix">
            <div className="float-left">
              <i className="mdi mdi-wunderlist text-success icon-lg"></i>
            </div>
            <div className="float-center">
              {/* <p className="mb-0 text-right text-dark"></p> */}
              <div className="fluid-container">
                <h3 className="font-weight-medium text-right mb-0 mt-3 text-dark">
                  <Link className="nav-link" to="/postsfeed">
                    {/* <i className="mdi mdi-image menu-icon"></i> */}
                    <span className="menu-title">Posts Feed</span>
                  </Link>
                </h3>
              </div>
            </div>
          </div>
          {this.props.showReport ? (
            <div className="clearfix">
              <div className="float-left">
                <i className="mdi mdi-chart-bar text-warning icon-lg"></i>
              </div>
              <div className="float-right">
                {/* <p className="mb-0 text-right text-dark"></p> */}
                <div className="fluid-container">
                  <h3 className="font-weight-medium text-left mb-0 mt-3 text-dark">
                    <Link className="nav-link" to="/report/post-stats">
                      {/* <i className="mdi mdi-image menu-icon"></i> */}
                      <span className="menu-title">Campaign Report</span>
                    </Link>
                  </h3>
                </div>
              </div>
            </div>
          ) : null}
        </div>
      </div>
    );
  }
}

export default withRouter(ContentSlideCard);
