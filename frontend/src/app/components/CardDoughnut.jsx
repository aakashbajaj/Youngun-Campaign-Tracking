import React, { Component } from "react";
import { Doughnut } from "react-chartjs-2";

export default class CardDoughnut extends Component {
  getChartData(param1, param2) {
    return {
      datasets: [
        {
          data: [param1, param2],
          backgroundColor: ["#19d895", "#2196f3", "#dde4eb"],
          borderColor: ["#19d895", "#2196f3", "#dde4eb"],
        },
      ],
      labels: ["Approved", "Remaining"],
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
                data={this.getChartData(
                  this.props.approved_content_pieces,
                  this.props.remaining_content_pieces
                )}
                options={this.usersDoughnutChartOptions}
                width={180}
              />
            </div>
            <div className="col-md-7">
              {/* <h4 className="card-title font-weight-medium mb-2 d-none d-md-block">
                Participating Profiles: {this.props.unique_content_pieces}
                <p className="mb-0 font-weight-medium"></p>
              </h4>
              <h4 className="card-title font-weight-medium mb-0 d-none d-md-block">
                Unique Content Pieces: {this.props.unique_content_pieces}
                <p className="mb-0 font-weight-medium"></p>
              </h4> */}
              <div className="wrapper mt-2">
                <h4 className="card-title font-weight-medium mb-2 ">
                  Participating Profiles: {this.props.particaipating_profiles}
                  {/* <p className="mb-0 font-weight-medium"></p> */}
                </h4>
                <h4 className="card-title font-weight-medium mb-2 ">
                  Unique Content Pieces: {this.props.unique_content_pieces}
                  {/* <p className="mb-0 font-weight-medium"></p> */}
                </h4>

                {/* <ProgressBar variant="primary" now={80} /> */}
              </div>
              <div className="wrapper mt-3">
                <div className="d-flex justify-content-between mb-2">
                  <div className="d-flex align-items-center">
                    <p className="mb-0 font-weight-medium">
                      {this.props.approved_content_pieces}
                    </p>
                    <small className="text-muted ml-2">Approved</small>
                  </div>
                </div>
                <div className="d-flex justify-content-between mb-2">
                  <div className="d-flex align-items-center">
                    <p className="mb-0 font-weight-medium">
                      {this.props.remaining_content_pieces}
                    </p>
                    <small className="text-muted ml-2">Remaining</small>
                  </div>
                  {/* <p className="mb-0 font-weight-medium">34%</p> */}
                </div>
                {/* <ProgressBar variant="success" now={34} /> */}
              </div>
            </div>
          </div>
        </div>
      </div>
    );
  }
}
