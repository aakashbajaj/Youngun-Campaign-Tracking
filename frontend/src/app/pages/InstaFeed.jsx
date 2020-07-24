import React, { Component } from "react";
import CampaignContext from "../data/CampaignContext";
import Spinner from "../shared/Spinner";

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
    return (
      <div>
        <div className="page-header">
          <h3 className="page-title">Instagram</h3>
        </div>
        <div className="container">
          <div className="card-columns">
            {instaposts.map((post, idx) => {
              if (post.embed_code !== "") {
                return (
                  <div className="columns">
                    <div className="decks">
                      <div
                        dangerouslySetInnerHTML={this.createMarkup(
                          post.embed_code
                        )}
                      />
                    </div>
                  </div>
                );
              }
              return null;
            })}
          </div>
        </div>
      </div>
    );
  }
}
