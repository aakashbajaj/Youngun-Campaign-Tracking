import React, { Component } from "react";

import CampaignContext from "../data/CampaignContext";
import StoryMetric from "../components/StoryMetric";
import Spinner from "../shared/Spinner";
import ContentSlideCard from "../components/ContentSlideCard";
import InviteUserCard from "../components/InviteUserCard";
import Reporting from "./Reporting";
// import ContentSlideCard from "../components/ContentSlideCard";
// import DatePicker from 'react-datepicker';
// import { Dropdown } from 'react-bootstrap';

export class Dashboard extends Component {
  static contextType = CampaignContext;

  currentCampLiveMetricsTemp = {
    name: "",
    brand: {
      name: "",
    },
    hashtag: "",
    status: "",

    start_date: "",
    end_date: "",

    slide_url: "",
    live_google_sheet: "",
    slug: "",

    particaipating_profiles: "",
    unique_content_pieces: "",
    approved_content_pieces: "",
    remaining_content_pieces: "",

    last_updated: "",

    fb_posts: "",
    fb_stories: "",

    in_posts: "",
    in_stories: "",

    tw_posts: "",
    tw_stories: "",

    // live_fb_posts: "",
    // live_fb_stories: "",

    // live_in_posts: "",
    // live_in_stories: "",

    // live_tw_posts: "",
    // live_tw_stories: "",

    live_fb_posts_cnt: "",
    live_fb_stories_cnt: "",

    live_in_posts_cnt: "",
    live_in_stories_cnt: "",

    live_tw_posts_cnt: "",
    live_tw_stories_cnt: "",
  };
  componentDidMount() {
    // this.setState({ currentCampaign: this.context.currentCampaignInView });
    // const liveCampMetrics = this.context.liveCampaignData[
    //   this.context.currentCampaignInView
    // ];
    // this.setState({ currentCampLiveMetrics: liveCampMetrics });
  }

  toggleProBanner() {
    document.querySelector(".proBanner").classList.toggle("hide");
  }

  zeroToDash(cnt) {
    if (cnt === 0) {
      return "--";
    }
    return cnt;
  }

  render() {
    var liveCampMetrics = this.currentCampLiveMetrics;
    var showReport = false;
    var showCosts = false;

    var currentCampaignInView = this.context.currentCampaignInView;

    if (currentCampaignInView) {
      if (this.context.campaigns[currentCampaignInView]) {
        if (
          this.context.campaigns[currentCampaignInView].campaign_module === "v2"
        ) {
          showReport = true;
        }
      }
    }

    if (currentCampaignInView) {
      if (this.context.campaigns[currentCampaignInView]) {
        if (
          this.context.campaigns[currentCampaignInView].campaign_module === "v2"
        ) {
          if (
            this.context.campaigns[currentCampaignInView].status === "completed"
          )
            showCosts = true;
        }
      }
    }

    if (
      this.context.currentCampaignInView &&
      this.context.liveCampaignData[this.context.currentCampaignInView]
    ) {
      liveCampMetrics = this.context.liveCampaignData[
        this.context.currentCampaignInView
      ];
    } else {
      liveCampMetrics = this.currentCampLiveMetrics;
    }
    console.log(liveCampMetrics);
    if (this.context.campaignCount === 0) {
      console.log(this.context.campaignCount);
      return <h5>No Data To Show</h5>;
    } else if (!liveCampMetrics) {
      return <Spinner />;
    }
    return (
      <div>
        <div className="page-header">
          <h3 className="page-title">
            {liveCampMetrics && liveCampMetrics.brand
              ? liveCampMetrics.brand.name
              : null}
          </h3>
          <nav aria-label="breadcrumb">
            <ol className="breadcrumb">
              <li className="breadcrumb-item">
                {liveCampMetrics ? (
                  <a
                    href={`https://www.instagram.com/explore/tags/${liveCampMetrics.hashtag}/`}
                    target="_blank"
                    rel="noopener noreferrer"
                    // onClick={(event) => event.preventDefault()}
                  >
                    #{liveCampMetrics.hashtag}
                  </a>
                ) : null}
              </li>
            </ol>
          </nav>
        </div>
        <div className="row">
          <div className="col-xl-4 col-lg-6 col-md-6 col-sm-6 grid-margin stretch-card">
            {/* Instagram */}
            <StoryMetric
              platform="in"
              PostMainText={`Posts Live: ${this.zeroToDash(
                liveCampMetrics.live_in_posts_cnt
              )}`}
              PostSubText={`Total Posts: ${this.zeroToDash(
                liveCampMetrics.in_posts
              )}`}
              StoryMainText={`Stories Live: ${this.zeroToDash(
                liveCampMetrics.live_in_stories_cnt
              )}`}
              StorySubText={`Total Stories: ${this.zeroToDash(
                liveCampMetrics.in_stories
              )}`}
            />
          </div>
          <div className="col-xl-4 col-lg-6 col-md-6 col-sm-6 grid-margin stretch-card">
            {/* Facebook */}
            <StoryMetric
              platform="fb"
              PostMainText={`Posts Live: ${this.zeroToDash(
                liveCampMetrics.live_fb_posts_cnt
              )}`}
              PostSubText={`Total Posts: ${this.zeroToDash(
                liveCampMetrics.fb_posts
              )}`}
              StoryMainText={`Stories Live: ${this.zeroToDash(
                liveCampMetrics.live_fb_stories_cnt
              )}`}
              StorySubText={`Total Stories: ${this.zeroToDash(
                liveCampMetrics.fb_stories
              )}`}
            />
          </div>
          <div className="col-xl-4 col-lg-6 col-md-6 col-sm-6 grid-margin stretch-card">
            {/* Twitter */}
            <StoryMetric
              platform="tw"
              PostMainText={`Posts Live: ${this.zeroToDash(
                liveCampMetrics.live_tw_posts_cnt
              )}`}
              PostSubText={`Total Posts: ${this.zeroToDash(
                liveCampMetrics.tw_posts
              )}`}
              StoryMainText={`Stories Live: ${this.zeroToDash(
                liveCampMetrics.live_tw_stories_cnt
              )}`}
              StorySubText={`Total Stories: ${this.zeroToDash(
                liveCampMetrics.tw_stories
              )}`}
            />
          </div>
        </div>

        {/* <div className="row">
          <div className="col-xl-4 col-lg-6 col-sm-6  grid-margin stretch-card">
            C5
          </div>
          <div className="col-xl-4 col-lg-6 col-sm-6 grid-margin stretch-card">
            CC
          </div>
          <div className="col-xl-4 col-lg-12 col-sm-12 grid-margin stretch-card">
            <div className="row flex-grow">
              <div className="col-xl-12 col-lg-6 col-sm-6 grid-margin-0 grid-margin-xl stretch-card">
                CC
              </div>
              <div className="col-xl-12 col-lg-6 col-sm-6 stretch-card">
                CC
              </div>
            </div>
          </div>
        </div> */}
        <div className="row">
          <div className="col-sm-6 col-md-6 col-lg-6 grid-margin stretch-card">
            <Reporting
              total_posts={liveCampMetrics.live_posts_cnt}
              in_num={liveCampMetrics.live_in_posts_cnt}
              tw_num={liveCampMetrics.live_tw_posts_cnt}
              fb_num={liveCampMetrics.live_fb_posts_cnt}
              in_eng={liveCampMetrics.in_engagement}
              tw_eng={liveCampMetrics.tw_engagement}
              fb_eng={liveCampMetrics.fb_engagement}
              in_reach={liveCampMetrics.in_reach}
              tw_reach={liveCampMetrics.tw_reach}
              fb_reach={liveCampMetrics.fb_reach}
              showCosts={showCosts}
            />
          </div>
          <div className="col-sm-6 col-md-6 col-lg-6">
            <div className="row">
              <div className="col-sm-12 col-md-12 col-lg-12 grid-margin stretch-card">
                <ContentSlideCard showReport={showReport} />
              </div>
            </div>
            <div className="row">
              {this.context.user.is_main_user ? (
                <div className="col-sm-12 col-md-12 col-lg-12 grid-margin stretch-card">
                  <InviteUserCard />
                </div>
              ) : null}
            </div>
            {/* <div className="row">
              <div className="col-sm-8 col-md-8 col-lg-8 grid-margin stretch-card">
                <PostDistGraph
                  in_num={liveCampMetrics.live_in_posts_cnt}
                  tw_num={liveCampMetrics.live_tw_posts_cnt}
                  fb_num={liveCampMetrics.live_fb_posts_cnt}
                />
              </div>
            </div>
            <div className="row">
              <div className="col-sm-8 col-md-8 col-lg-8 grid-margin stretch-card">
                <EngReachDoughnut
                  in_eng={liveCampMetrics.in_engagement}
                  tw_eng={liveCampMetrics.tw_engagement}
                  fb_eng={liveCampMetrics.fb_engagement}
                  in_reach={liveCampMetrics.in_reach}
                  tw_reach={liveCampMetrics.tw_reach}
                  fb_reach={liveCampMetrics.fb_reach}
                />
              </div>
            </div> */}
          </div>
          {/* <div className="col-sm-6 col-md-6 col-lg-6 grid-margin stretch-card"></div> */}
        </div>
      </div>
    );
  }
}
export default Dashboard;
