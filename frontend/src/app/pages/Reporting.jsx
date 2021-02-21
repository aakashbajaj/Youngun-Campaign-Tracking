import React, { Component } from "react";

import CampaignContext from "../data/CampaignContext";
import StoryMetric from "../components/StoryMetric";
import CardDoughnut from "../components/CardDoughnut";
import Spinner from "../shared/Spinner";
import PostListTable from "../components/PostListTable";
import PostDistGraph from "../components/PostDistgraph";
import EngReachDoughnut from "../components/EngReachDoughnut";

export default class Reporting extends Component {
  static contextType = CampaignContext;
  render() {
    if (this.context.currentCampaignInView === null) {
      return <Spinner />;
    }
    var campReportData = [];
    if (this.context.currentCampaignInView) {
      if (this.context.campaignReportData) {
        if (
          this.context.campaignReportData[this.context.currentCampaignInView]
        ) {
          campReportData = this.context.campaignReportData[
            this.context.currentCampaignInView
          ];
        }
      }
    }

    return (
      <div>
        <div className="row">
          {/* Number of Live Posts */}
          <div className="col-xl-4 col-lg-4 col-md-12 col-sm-12 grid-margin stretch-card">
            <div className="card">
              <div className="card-body py-4">
                <div className="d-flex flex-row justify-content-center align-items">
                  <i
                    className={`mdi mt-lg-5 mt-sm-2 ml-3 mdi-account-box-multiple text-warning icon-lg`}
                  ></i>
                  <div className="ml-4">
                    {/* <p className="text-muted card-text mt-2 mb-1">₹ 0.34</p> */}
                    <h6 className={`font-weight-semibold mt-lg-5 mt-sm-2 mb-1`}>
                      Number of Posts
                    </h6>
                    <h6 className={`font-weight-bold mt-2`}>
                      {this.props.total_posts}
                    </h6>
                  </div>
                  {/* <div className="ml-2"></div> */}
                </div>
              </div>
            </div>
          </div>

          {/* Live Posts Graphs */}
          <div className="col-xl-8 col-lg-8 col-md-12 col-sm-12 grid-margin stretch-card">
            <PostDistGraph
              in_num={this.props.in_num}
              tw_num={this.props.tw_num}
              fb_num={this.props.fb_num}
            />
          </div>

          <div className="col-xl-4 col-lg-4 col-md-12 col-sm-12">
            <div className="row">
              <div className="col-xl-12 col-lg-12 col-md-12 col-sm-12 grid-margin stretch-card">
                <div className="card">
                  <div className="card-body py-4">
                    <div className="d-flex flex-row justify-content-center align-items">
                      <i className={`mdi mdi-lan text-info icon-lg`}></i>
                      <div className="ml-4">
                        {/* <p className="text-muted card-text mt-2 mb-1">₹ 0.34</p> */}
                        <h6 className={`font-weight-semibold mt-2 mb-1`}>
                          Total Campaign
                          <br />
                          Enagagement
                        </h6>
                        <h6 className={`font-weight-bold mt-2`}>
                          {campReportData.total_post_engagement}
                        </h6>
                      </div>
                      {/* <div className="ml-2"></div> */}
                    </div>
                  </div>
                </div>
              </div>
            </div>
            <div className="row">
              <div className="col-xl-12 col-lg-12 col-md-12 col-sm-12 grid-margin stretch-card">
                <div className="card">
                  <div className="card-body py-4">
                    <div className="d-flex flex-row justify-content-center align-items">
                      <i
                        className={`mdi mdi-human-greeting text-success icon-lg`}
                      ></i>
                      <div className="ml-4">
                        {/* <p className="text-muted card-text mt-2 mb-1">₹ 0.34</p> */}
                        <h6 className={`font-weight-semibold mt-2 mb-1`}>
                          Total Campaign
                          <br />
                          Reach
                        </h6>
                        <h6 className={`font-weight-bold mt-2`}>
                          {campReportData.total_campaign_reach}
                        </h6>
                      </div>
                      {/* <div className="ml-2"></div> */}
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>

          {/* Post Engagement */}
          <div className="col-xl-8 col-lg-8 col-md-12 col-sm-12 grid-margin stretch-card">
            <EngReachDoughnut
              in_eng={this.props.in_eng}
              tw_eng={this.props.tw_eng}
              fb_eng={this.props.fb_eng}
              in_reach={this.props.in_reach}
              tw_reach={this.props.tw_reach}
              fb_reach={this.props.fb_reach}
            />
          </div>

          {/* Post Shares */}
          {/* <div className="col-xl-6 col-lg-6 col-md-12 col-sm-12 grid-margin stretch-card">
            <div className="card">
              <div className="card-body py-4">
                <div className="d-flex flex-row justify-content-center align-items">
                  <i className={`mdi mdi-share text-info icon-lg`}></i>
                  <div className="ml-4">
                  
                    <h6 className={`font-weight-semibold mt-2 mb-1`}>
                      Post Shares
                    </h6>
                    <h6 className={`font-weight-bold mt-2`}>
                      {campReportData.post_shares}
                    </h6>
                  </div>
                  
                </div>
              </div>
            </div>
          </div> */}

          {/* Post Saves */}
          {/* <div className="col-xl-6 col-lg-6 col-md-12 col-sm-12 grid-margin stretch-card">
            <div className="card">
              <div className="card-body py-4">
                <div className="d-flex flex-row justify-content-center align-items">
                  <i
                    className={`mdi mdi-content-save-all text-danger icon-lg`}
                  ></i>
                  <div className="ml-4">
                    
                    <h6 className={`font-weight-semibold mt-2 mb-1`}>
                      Post Saves
                    </h6>
                    <h6 className={`font-weight-bold mt-2`}>
                      {campReportData.post_saves}
                    </h6>
                  </div>
                </div>
              </div>
            </div>
          </div> */}

          {/* Video Views */}
          {/* <div className="col-xl-6 col-lg-6 col-md-12 col-sm-12 grid-margin stretch-card">
            <div className="card">
              <div className="card-body py-4">
                <div className="d-flex flex-row justify-content-center align-items">
                  <i className={`mdi mdi-video text-warning icon-lg`}></i>
                  <div className="ml-4">
                  
                    <h6 className={`font-weight-semibold mt-2 mb-1`}>
                      Video Views
                    </h6>
                    <h6 className={`font-weight-bold mt-2`}>
                      {campReportData.video_views}
                    </h6>
                  </div>
                  
                </div>
              </div>
            </div>
          </div> */}

          {/* Static Post Reach */}
          {/* <div className="col-xl-6 col-lg-6 col-md-12 col-sm-12 grid-margin stretch-card">
            <div className="card">
              <div className="card-body py-4">
                <div className="d-flex flex-row justify-content-center align-items">
                  <i className={`mdi mdi-airplane text-success icon-lg`}></i>
                  <div className="ml-4">
                    <h6 className={`font-weight-semibold mt-2 mb-1`}>
                      Static Post Reach
                    </h6>
                    <h6 className={`font-weight-bold mt-2`}>
                      {campReportData.post_reach}
                    </h6>
                  </div>
                </div>
              </div>
            </div>
          </div> */}

          {this.props.showCosts &&
          campReportData.cost_per_reach !== "" &&
          campReportData.cost_per_engagement !== "" ? (
            <div className="col-xl-12 col-lg-12 col-md-12 col-sm-12 grid-margin stretch-card">
              <div className="col-xl-6 col-lg-6 col-md-12 col-sm-12 grid-margin stretch-card">
                <div className="card">
                  <div className="card-body py-4">
                    <div className="d-flex flex-row justify-content-center align-items">
                      <i className={`mdi mdi-receipt text-info icon-lg`}></i>
                      <div className="ml-4">
                        {/* <p className="text-muted card-text mt-2 mb-1">₹ 0.34</p> */}
                        <h6 className={`font-weight-semibold mt-2 mb-1`}>
                          Cost Per Reach
                        </h6>
                        <h6 className={`font-weight-bold mt-2`}>
                          {campReportData.cost_per_reach}
                        </h6>
                      </div>
                      {/* <div className="ml-2"></div> */}
                    </div>
                  </div>
                </div>
              </div>

              <div className="col-xl-6 col-lg-6 col-md-12 col-sm-12 grid-margin stretch-card">
                <div className="card">
                  <div className="card-body py-4">
                    <div className="d-flex flex-row justify-content-center align-items">
                      <i className={`mdi mdi-receipt text-danger icon-lg`}></i>
                      <div className="ml-4">
                        {/* <p className="text-muted card-text mt-2 mb-1">₹ 0.34</p> */}
                        <h6 className={`font-weight-semibold mt-2 mb-1`}>
                          Cost Per <br />
                          Engagement
                        </h6>
                        <h6 className={`font-weight-bold mt-2`}>
                          {campReportData.cost_per_engagement}
                        </h6>
                      </div>
                      {/* <div className="ml-2"></div> */}
                    </div>
                  </div>
                </div>
              </div>
            </div>
          ) : null}
        </div>
      </div>
    );
  }
}
