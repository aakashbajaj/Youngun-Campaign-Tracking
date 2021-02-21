import React, { Component } from "react";
import { Doughnut } from "react-chartjs-2";

export default class PostDistGraph extends Component {
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

    // console.log(data);
    // console.log(backgroundColor);
    // console.log(labels);

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
  render() {
    return (
      <div className="card">
        <div className="card-body">
          <div className="row">
            <div className="col-md-5 d-flex align-items-center">
              <Doughnut
                data={this.genChartData(
                  this.props.in_num,
                  this.props.tw_num,
                  this.props.fb_num
                )}
                options={this.usersDoughnutChartOptions}
                width={180}
              />
            </div>
            <div className="col-md-7">
              <h4 className="card-title font-weight-bold mb-3 mt-2">
                Post Distribution
              </h4>
              {/* <h4 className="card-title font-weight-medium mb-2 d-none d-md-block">
                Participating Profiles: {this.props.unique_content_pieces}
                <p className="mb-0 font-weight-medium"></p>
              </h4>
              <h4 className="card-title font-weight-medium mb-0 d-none d-md-block">
                Unique Content Pieces: {this.props.unique_content_pieces}
                <p className="mb-0 font-weight-medium"></p>
              </h4> */}
              <div className="wrapper mt-2">
                {/* <h4 className="card-title font-weight-medium mb-2 ">
                  Participating Profiles: {this.props.particaipating_profiles}
                </h4>
                <h4 className="card-title font-weight-medium mb-2 ">
                  Unique Content Pieces: {this.props.unique_content_pieces}
                </h4> */}

                <table className="table table-hover table-striped">
                  <tbody>
                    {this.props.in_num > 0 ? (
                      <tr>
                        <td>Instagram:</td>
                        <td>{this.props.in_num}</td>
                      </tr>
                    ) : null}

                    {this.props.tw_num > 0 ? (
                      <tr>
                        <td>Twitter:</td>
                        <td>{this.props.tw_num}</td>
                      </tr>
                    ) : null}

                    {this.props.fb_num > 0 ? (
                      <tr>
                        <td>Facebook:</td>
                        <td>{this.props.fb_num}</td>
                      </tr>
                    ) : null}
                  </tbody>
                </table>
                {/* {this.props.in_num > 0 ? (
                  <h4 className="card-title font-weight-light mb-3 ">
                    Instagram:
                    <span className="font-weight-medium">
                      {this.props.in_num}
                    </span>
                  </h4>
                ) : null}

                {this.props.tw_num > 0 ? (
                  <h4 className="card-title font-weight-light mb-3 ">
                    Twitter:
                    <span className="font-weight-medium">
                      {this.props.tw_num}
                    </span>
                  </h4>
                ) : null}

                {this.props.fb_num > 0 ? (
                  <h4 className="card-title font-weight-light mb-3 ">
                    Facebook:
                    <span className="font-weight-medium">
                      {this.props.fb_num}
                    </span>
                  </h4>
                ) : null} */}

                {/* <ProgressBar variant="primary" now={80} /> */}
              </div>
            </div>
          </div>
        </div>
      </div>
    );
  }
}
