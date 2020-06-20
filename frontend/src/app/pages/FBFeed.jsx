import React, { Component } from "react";
import CampaignContext from "../data/CampaignContext";
import Spinner from "../shared/Spinner";

export default class FBFeed extends Component {
  static contextType = CampaignContext;

  createMarkup(embed_code) {
    return { __html: embed_code };
  }
  componentDidMount() {
    console.log("in FB CDM");
    window.fbAsyncInit();
  }

  componentDidUpdate(prevProps, prevState) {
    window.instgrm.Embeds.process();
    window.fbAsyncInit();
  }

  render() {
    var fbposts = [];
    if (
      this.context.currentCampaignInView !== null &&
      this.context.liveCampaignFeed[this.context.currentCampaignInView] !==
        null &&
      this.context.liveCampaignFeed[this.context.currentCampaignInView]
        .facebook !== null
    ) {
      fbposts = this.context.liveCampaignFeed[
        this.context.currentCampaignInView
      ].facebook;
    }

    if (!fbposts) {
      return <Spinner />;
    }
    return (
      <div>
        <div className="page-header">
          <h3 className="page-title">Facebook</h3>
        </div>
        <div className="row">
          {fbposts.map((post, idx) => {
            return (
              <div className="col-xl-6 col-lg-6 col-md-6 col-sm-6 grid-margin stretch-card">
                <div
                  className="fb-post"
                  data-href={`${post.url}`}
                  data-width="100"
                ></div>
              </div>
            );
          })}
        </div>
      </div>
    );
  }
}
