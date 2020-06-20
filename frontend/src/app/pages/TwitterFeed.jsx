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
    window.instgrm.Embeds.process();
  }

  componentDidUpdate(prevProps, prevState) {
    window.instgrm.Embeds.process();
  }

  render() {
    var instaposts = [];
    if (
      this.context.currentCampaignInView !== null &&
      this.context.liveCampaignFeed[this.context.currentCampaignInView] !==
        null &&
      this.context.liveCampaignFeed[this.context.currentCampaignInView]
        .instagram !== null
    ) {
      instaposts = this.context.liveCampaignFeed[
        this.context.currentCampaignInView
      ].instagram;
    }

    if (!instaposts) {
      return <Spinner />;
    }
    return (
      <div>
        <div className="page-header">
          <h3 className="page-title">Instagram/Facebook/Twitter</h3>
        </div>
        <div className="row">
          {instaposts.map((post, idx) => {
            if (post.embed_code !== "") {
              return (
                <div className="col-xl-4 col-lg-6 col-md-6 col-sm-6 grid-margin stretch-card">
                  <div
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
