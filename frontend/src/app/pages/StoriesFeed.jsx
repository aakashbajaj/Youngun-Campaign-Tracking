import React, { Component } from "react";
import CampaignContext from "../data/CampaignContext";
import Spinner from "../shared/Spinner";

export default class StoriesFeed extends Component {
  static contextType = CampaignContext;

  createMarkup(embed_code) {
    return { __html: embed_code };
  }
  componentDidMount() {
    console.log("in Stories CDM");
    // window.fbAsyncInit();
  }

  componentDidUpdate(prevProps, prevState) {
    // window.instgrm.Embeds.process();
    // window.fbAsyncInit();
  }

  render() {
    var stories_url = "";
    if (
      this.context.currentCampaignInView !== null &&
      this.context.liveCampaignFeed[this.context.currentCampaignInView] !==
        null &&
      this.context.liveCampaignFeed[this.context.currentCampaignInView]
        .stories_google_photos_album_url !== null
    ) {
      stories_url = this.context.liveCampaignFeed[
        this.context.currentCampaignInView
      ].stories_google_photos_album_url;
    }

    if (!stories_url) {
      return <Spinner />;
    } else if (stories_url === "") {
      return <div>Nothing to show</div>;
    }
    const iframe_str = `<iframe src=${stories_url}></iframe>`;
    return (
      <div>
        <div className="page-header">
          <h3 className="page-title">Stories</h3>
        </div>
        <div className="row">
          <div>
            <div dangerouslySetInnerHTML={this.createMarkup(iframe_str)}></div>
          </div>
          {/* {fbposts.map((post, idx) => {
            return (
              <div
                key={idx}
                className="col-xl-6 col-lg-6 col-md-6 col-sm-6 grid-margin stretch-card"
              >
                <div
                  className="fb-post"
                  data-href={`${post.url}`}
                  data-width="100"
                ></div>
              </div>
            );
          })} */}
        </div>
      </div>
    );
  }
}
