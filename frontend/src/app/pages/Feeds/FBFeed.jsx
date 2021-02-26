import React, { Component } from "react";
import CampaignContext from "../../data/CampaignContext";
import Spinner from "../../shared/Spinner";

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
        {/* <div className="card-columns"> */}
        <div className="row">
          {fbposts.map((post, idx) => {
            return (
              <div
                key={idx}
                className="col-xl-4 col-lg-4 col-md-6 col-sm-12 grid-margin stretch-card"
                // className="card"
              >
                {post.post_type === "p" ? (
                  <div
                    className="fb-post"
                    data-href={`${post.url}`}
                    data-width="400"
                  />
                ) : (
                  <div
                    class="fb-video"
                    data-href={`${post.url}`}
                    data-width="400"
                    data-allowfullscreen="true"
                    data-autoplay="false"
                    data-show-captions="true"
                  />
                )}

                {/* </div> */}
              </div>
            );
          })}
        </div>
      </div>
      // </div>
    );
  }
}
