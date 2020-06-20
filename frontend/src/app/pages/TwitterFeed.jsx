import React, { Component } from "react";
import CampaignContext from "../data/CampaignContext";
import Spinner from "../shared/Spinner";

export default class TwitterFeed extends Component {
  static contextType = CampaignContext;

  createMarkup(embed_code) {
    return { __html: embed_code };
  }
  componentDidMount() {
    console.log("in FB CDM");
    window.twttr.widgets.load(document.getElementById("twitter-post"));
  }

  componentDidUpdate(prevProps, prevState) {
    window.twttr.widgets.load(document.getElementById("twitter-post"));
  }

  render() {
    var twitterposts = [];
    if (
      this.context.currentCampaignInView !== null &&
      this.context.liveCampaignFeed[this.context.currentCampaignInView] !==
        null &&
      this.context.liveCampaignFeed[this.context.currentCampaignInView]
        .twitter !== null
    ) {
      twitterposts = this.context.liveCampaignFeed[
        this.context.currentCampaignInView
      ].twitter;
    }

    if (!twitterposts) {
      return <Spinner />;
    }
    return (
      <div>
        <div className="page-header">
          <h3 className="page-title">Twitter</h3>
        </div>
        <div className="row">
          {twitterposts.map((post, idx) => {
            if (post.embed_code !== "") {
              return (
                <div key={idx}>
                  <div
                    className="col-xl-6 col-lg-6 col-md-6 col-sm-12 grid-margin stretch-card"
                    dangerouslySetInnerHTML={this.createMarkup(post.embed_code)}
                  />
                </div>
              );
            }
            return null;
          })}
        </div>
      </div>
    );
  }
}
