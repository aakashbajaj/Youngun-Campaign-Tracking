import React, { Component } from "react";
import CampaignContext from "../data/CampaignContext";
import Spinner from "../shared/Spinner";

import "./Masonry.css";

import Masonry from "react-masonry-component";

const masonryOptions = {
  transitionDuration: 0,
  columnWidth: 3,
};

const imagesLoadedOptions = { background: ".my-bg-image-el" };

export default class InstaFeed extends Component {
  static contextType = CampaignContext;

  createMarkup(embed_code) {
    return { __html: embed_code };
  }
  componentDidMount() {
    // if (width <= 768) {
    //   $(".card-columns").removeClass("card-columns").addClass("row");
    //   $(".columns").addClass("col-sm-12");
    //   $(".decks").addClass("card-deck pb-5");
    // } else {
    //   $(".row").addClass("card-columns").removeClass("row");
    //   $(".columns").removeClass("col-sm-12");
    //   $(".decks").removeClass("card-deck pb-5");
    // }

    console.log("in Insta CDM");
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

    const childElements = instaposts.map((post, idx) => {
      if (post.embed_code !== "") {
        return (
          <div className="masonry-item">
            <div dangerouslySetInnerHTML={this.createMarkup(post.embed_code)} />
          </div>
        );
      }
      // return null;
    });

    return (
      <div>
        <div className="masonry">{childElements}</div>;
      </div>
    );
  }
}
