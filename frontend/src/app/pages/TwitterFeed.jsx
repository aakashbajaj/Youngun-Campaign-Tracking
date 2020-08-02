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
    window.twttr.widgets.load();
  }

  componentDidUpdate(prevProps, prevState) {
    window.twttr.widgets.load();
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
        <div className="row">
          {/* <div className="card-columns"> */}
          {twitterposts.map((post, idx) => {
            if (post.embed_code !== "") {
              return (
                <div key={idx}>
                  <div
                    className="col-xl-4 col-lg-4 col-md-6 col-sm-12 grid-margin stretch-card"
                    dangerouslySetInnerHTML={this.createMarkup(post.embed_code)}
                  />
                  {/* <div key={idx} className="card">
                  <div
                    dangerouslySetInnerHTML={this.createMarkup(post.embed_code)}
                  /> */}
                </div>
              );
            } else if (
              post.alt_google_photo_url !== "" &&
              post.alt_google_photo_url !== null
            ) {
              return (
                <div
                  key={idx}
                  className="col-xl-4 col-lg-4 col-md-6 col-sm-12 grid-margin stretch-card"
                >
                  <img
                    key={post.alt_google_photo_url}
                    src={post.alt_google_photo_url}
                    alt={"Post"}
                    href={post.url}
                    loader={<Spinner />}
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
