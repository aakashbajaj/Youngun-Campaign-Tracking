import React, { Component } from "react";

import CampaignContext from "../data/CampaignContext";
import StoryMetric from "../components/StoryMetric";
import CardDoughnut from "../components/CardDoughnut";
import Spinner from "../shared/Spinner";
import PostListTable from "../components/PostListTable";

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
          {/* Number of Content Pieces */}
          <div className="col-xl-3 col-lg-4 col-md-6 col-sm-6 grid-margin stretch-card">
            <div className="card">
              <div className="card-body py-4">
                <div className="d-flex flex-row justify-content-center align-items">
                  <i className={`mdi mdi-cube text-danger icon-lg`}></i>
                  <div className="ml-4">
                    {/* <p className="text-muted card-text mt-2 mb-1">₹ 0.34</p> */}
                    <h6 className={`font-weight-semibold mt-2 mb-1`}>
                      Number of <br />
                      Content Pieces
                    </h6>
                    <h6 className={`font-weight-bold mt-2`}>
                      {campReportData.num_content_pieces}
                    </h6>
                  </div>
                  {/* <div className="ml-2"></div> */}
                </div>
              </div>
            </div>
          </div>

          <div className="col-xl-3 col-lg-4 col-md-6 col-sm-6 grid-margin stretch-card">
            <div className="card">
              <div className="card-body py-4">
                <div className="d-flex flex-row justify-content-center align-items">
                  <i
                    className={`mdi mdi-account-box-multiple text-warning icon-lg`}
                  ></i>
                  <div className="ml-4">
                    {/* <p className="text-muted card-text mt-2 mb-1">₹ 0.34</p> */}
                    <h6 className={`font-weight-semibold mt-2 mb-1`}>
                      Number of Posts
                    </h6>
                    <h6 className={`font-weight-bold mt-2`}>
                      {campReportData.num_posts}
                    </h6>
                  </div>
                  {/* <div className="ml-2"></div> */}
                </div>
              </div>
            </div>
          </div>

          {/* Post Engagement */}
          <div className="col-xl-3 col-lg-4 col-md-6 col-sm-6 grid-margin stretch-card">
            <div className="card">
              <div className="card-body py-4">
                <div className="d-flex flex-row justify-content-center align-items">
                  <i className={`mdi mdi-poll-box text-success icon-lg`}></i>
                  <div className="ml-4">
                    {/* <p className="text-muted card-text mt-2 mb-1">₹ 0.34</p> */}
                    <h6 className={`font-weight-semibold mt-2 mb-1`}>
                      Post Engagement
                    </h6>
                    <h6 className={`font-weight-bold mt-2`}>
                      {campReportData.post_engagement}
                    </h6>
                  </div>
                  {/* <div className="ml-2"></div> */}
                </div>
              </div>
            </div>
          </div>

          {/* Post Shares */}
          {/* <div className="col-xl-3 col-lg-4 col-md-6 col-sm-6 grid-margin stretch-card">
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
          {/* <div className="col-xl-3 col-lg-4 col-md-6 col-sm-6 grid-margin stretch-card">
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
          {/* <div className="col-xl-3 col-lg-4 col-md-6 col-sm-6 grid-margin stretch-card">
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
          {/* <div className="col-xl-3 col-lg-4 col-md-6 col-sm-6 grid-margin stretch-card">
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

          <div className="col-xl-3 col-lg-4 col-md-6 col-sm-6 grid-margin stretch-card">
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

          <div className="col-xl-3 col-lg-4 col-md-6 col-sm-6 grid-margin stretch-card">
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

          <div className="col-xl-3 col-lg-4 col-md-6 col-sm-6 grid-margin stretch-card">
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

          <div className="col-xl-3 col-lg-4 col-md-6 col-sm-6 grid-margin stretch-card">
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

          <div className="col-xl-3 col-lg-4 col-md-6 col-sm-6 grid-margin stretch-card">
            <div className="card card-revenue">
              <a
                href="https://forms.gle/EiLXkNfhuBMHWhff8"
                target="_blank"
                rel="noopener noreferrer"
              >
                <div className="card-body">
                  <div className="d-flex w-100 h-100 justify-content-between align-items-center">
                    <div className="mr-auto">
                      <p className="highlight-text text-white">
                        {" "}
                        Add Post Inventory{" "}
                      </p>
                      {/* <p className="text-white"> This Month </p> */}
                      <div className="badge badge-pill mr-5">+</div>
                    </div>
                  </div>
                </div>
              </a>
            </div>
          </div>
        </div>
      </div>
    );
  }
}
