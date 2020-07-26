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
        <div className="container">
          <div className="card-columns">
            {fbposts.map((post, idx) => {
              return (
                <div key={idx} className="columns">
                  <div className="decks">
                    <div
                      className="fb-post"
                      data-href={`${post.url}`}
                      data-width="100"
                    ></div>
                  </div>
                </div>
              );
            })}
          </div>
        </div>
      </div>
    );
  }
}
