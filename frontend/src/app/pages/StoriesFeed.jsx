import React, { Component } from "react";
import CampaignContext from "../data/CampaignContext";
import Spinner from "../shared/Spinner";
import Img from "react-image";

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

  onImgLoad = (evt) => {
    evt.preventDeafult();
    // this.setState({ :  });
  };

  render() {
    var stories = [];
    if (
      this.context.currentCampaignInView !== null &&
      this.context.liveCampaignFeed[this.context.currentCampaignInView] !==
        null &&
      this.context.liveCampaignFeed[this.context.currentCampaignInView]
        .stories !== null
    ) {
      stories = this.context.liveCampaignFeed[
        this.context.currentCampaignInView
      ].stories;
    }

    if (!stories) {
      return <Spinner />;
    } else if (stories === []) {
      return <div>Nothing to show</div>;
    }
    // const iframe_str = `<iframe src=${stories_url}></iframe>`;
    return (
      <div>
        <div className="page-header">
          <h3 className="page-title">Stories</h3>
        </div>
        <div className="row">
          {/* <div>
            <div dangerouslySetInnerHTML={this.createMarkup(iframe_str)}></div>
          </div> */}
          {stories.map((post, idx) => {
            return (
              <div
                key={idx}
                className="col-xl-4 col-lg-4 col-md-5 col-sm-6 grid-margin stretch-card "
              >
                <img
                  key={post.url}
                  src={post.url}
                  alt={"Story"}
                  loader={<Spinner />}
                />
              </div>
            );
          })}
        </div>
      </div>
    );
  }
}
