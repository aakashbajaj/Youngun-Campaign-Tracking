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
    // var tw_coll_url = "";
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
      // tw_coll_url = this.context.liveCampaignFeed[
      //   this.context.currentCampaignInView
      // ].twitter_collection_url;
    }

    // if (!tw_coll_url) {
    //   return <Spinner />;
    // }
    if (!twitterposts) {
      return <Spinner />;
    }
    return (
      <div>
        <div className="row">
          {twitterposts.map((post, idx) => {
            if (post.embed_code !== "") {
              return (
                <div key={idx}>
                  <div
                    className="col-xl-4 col-lg-4 col-md-6 col-sm-12 grid-margin stretch-card"
                    dangerouslySetInnerHTML={this.createMarkup(post.embed_code)}
                  />
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
                  <a href={post.url} target="_blank" rel="noopener noreferrer">
                    <img
                      key={post.alt_google_photo_url}
                      src={post.alt_google_photo_url}
                      alt={"Post"}
                      loader={<Spinner />}
                    />
                  </a>
                </div>
              );
            }
            return null;
          })}
        </div>
        {/* <div className="row">
          <div className="col-xl-3 col-lg-3 col-md-2 hidden-sm"></div>
          <div
            className="col-xl-6 col-lg-6 col-md-6 col-sm-12"
            // style={{
            //   width: "50%",
            //   margin: "0 auto",
            // }}
          >
            <a class="twitter-timeline" data-width="550" href={tw_coll_url}></a>{" "}
            <script
              async
              src="https://platform.twitter.com/widgets.js"
              charset="utf-8"
            ></script>
          </div>
          <div className="col-xl-3 col-lg-3 col-md-2 hidden-sm"></div>
        </div> */}
      </div>
    );
  }
}
