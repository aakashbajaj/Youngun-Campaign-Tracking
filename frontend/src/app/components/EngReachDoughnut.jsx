import React, { Component } from "react";
import { Doughnut } from "react-chartjs-2";

export default class EngReachDoughnut extends Component {
  state = {
    currentMetric: "en",
  };

  genChartData(in_num, tw_num, fb_num) {
    var data = [];
    var backgroundColor = [];
    var labels = [];

    if (in_num > 0) {
      data.push(in_num);
      backgroundColor.push("#fbad50");
      labels.push("Instagram");
    }
    if (tw_num > 0) {
      data.push(tw_num);
      backgroundColor.push("#00acee");
      labels.push("Twitter");
    }
    if (fb_num > 0) {
      data.push(fb_num);
      backgroundColor.push("#4267B2");
      labels.push("Facebook");
    }

    console.log(data);
    console.log(backgroundColor);
    console.log(labels);

    return {
      datasets: [
        {
          data: data,
          backgroundColor: backgroundColor,
          borderColor: ["#fbad50", "#00acee", "#4267B2"],
        },
      ],
      labels: labels,
    };
  }

  usersDoughnutChartOptions = {
    cutoutPercentage: 70,
    animationEasing: "easeOutBounce",
    animateRotate: true,
    animateScale: false,
    responsive: true,
    maintainAspectRatio: true,
    showScale: true,
    legend: {
      display: false,
    },
    layout: {
      padding: {
        left: 0,
        right: 0,
        top: 0,
        bottom: 0,
      },
    },
  };

  selectMetric = (evt) => {
    evt.preventDefault();
    this.setState({ currentMetric: evt.target.id });
  };

  render() {
    var metrics, eng_btn_class, reach_btn_class;
    if (this.state.currentMetric === "en") {
      metrics = (
        <div>
          {this.props.in_eng > 0 ? (
            <h4 className="card-title font-weight-light mb-2 ">
              Instagram:
              <span className="font-weight-medium">{this.props.in_eng}</span>
            </h4>
          ) : null}

          {this.props.tw_eng > 0 ? (
            <h4 className="card-title font-weight-light mb-2 ">
              Twitter:
              <span className="font-weight-medium">{this.props.tw_eng}</span>
            </h4>
          ) : null}

          {this.props.fb_eng > 0 ? (
            <h4 className="card-title font-weight-light mb-2 ">
              Facebook:
              <span className="font-weight-medium">{this.props.fb_eng}</span>
            </h4>
          ) : null}
        </div>
      );
      eng_btn_class = "btn purchase-button";
      reach_btn_class = "btn download-button";
    } else {
      metrics = (
        <div>
          {this.props.in_reach > 0 ? (
            <h4 className="card-title font-weight-light mb-2 ">
              Instagram:
              <span className="font-weight-medium">{this.props.in_reach}</span>
            </h4>
          ) : null}

          {this.props.tw_reach > 0 ? (
            <h4 className="card-title font-weight-light mb-2 ">
              Twitter:
              <span className="font-weight-medium">{this.props.tw_reach}</span>
            </h4>
          ) : null}

          {this.props.fb_reach > 0 ? (
            <h4 className="card-title font-weight-light mb-2 ">
              Facebook:
              <span className="font-weight-medium">{this.props.fb_reach}</span>
            </h4>
          ) : null}
        </div>
      );
      eng_btn_class = "btn download-button";
      reach_btn_class = "btn purchase-button";
    }

    return (
      <div className="card">
        <div className="card-body">
          <div className="row">
            <div className="col-md-5 d-flex align-items-center">
              {this.state.currentMetric === "en" ? (
                <Doughnut
                  data={this.genChartData(
                    this.props.in_eng,
                    this.props.tw_eng,
                    this.props.fb_eng
                  )}
                  options={this.usersDoughnutChartOptions}
                  width={180}
                />
              ) : (
                <Doughnut
                  data={this.genChartData(
                    this.props.in_reach,
                    this.props.tw_reach,
                    this.props.fb_reach
                  )}
                  options={this.usersDoughnutChartOptions}
                  width={180}
                />
              )}
            </div>
            <div className="col-md-7">
              {/* <h4 className="card-title font-weight-bold mb-1 mt-2">
                Post Distribution
              </h4> */}
              <div className="row proBanner">
                <div className="col-8">
                  <span className="mt-2 d-flex purchase-popup align-items-center">
                    <div
                      id="en"
                      onClick={this.selectMetric}
                      className={eng_btn_class}
                    >
                      Engagement
                    </div>
                    <div
                      id="rch"
                      onClick={this.selectMetric}
                      className={reach_btn_class}
                    >
                      Reach
                    </div>
                  </span>
                </div>
              </div>
              {/* <h4 className="card-title font-weight-medium mb-2 d-none d-md-block">
                Participating Profiles: {this.props.unique_content_pieces}
                <p className="mb-0 font-weight-medium"></p>
              </h4>
              <h4 className="card-title font-weight-medium mb-0 d-none d-md-block">
                Unique Content Pieces: {this.props.unique_content_pieces}
                <p className="mb-0 font-weight-medium"></p>
              </h4> */}
              <div className="wrapper mt-1">
                {/* <h4 className="card-title font-weight-medium mb-2 ">
                  Participating Profiles: {this.props.particaipating_profiles}
                </h4>
                <h4 className="card-title font-weight-medium mb-2 ">
                  Unique Content Pieces: {this.props.unique_content_pieces}
                </h4> */}

                {metrics}

                {/* <ProgressBar variant="primary" now={80} /> */}
              </div>
            </div>
          </div>
        </div>
      </div>
    );
  }
}
