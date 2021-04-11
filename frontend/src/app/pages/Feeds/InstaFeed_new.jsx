import React, { Component } from "react";
import CampaignContext from "../../data/CampaignContext";
import Spinner from "../../shared/Spinner";
import Masonry, { ResponsiveMasonry } from "react-responsive-masonry";

export default class InstaFeed extends Component {
  static contextType = CampaignContext;

  constructor(props) {
    super(props);
    this.state = {
      reRender: false,
      containerId: "bricks-container-app",
      hasMoreBricks: false,
    };
  }

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
      this.context.currentCampaignInView &&
      this.context.liveCampaignFeed[this.context.currentCampaignInView]
    ) {

      if (this.context.liveCampaignFeed[this.context.currentCampaignInView]
        .instagram) {
        instaposts = this.context.liveCampaignFeed[
          this.context.currentCampaignInView
        ].instagram;
      }

      else{
        return <Spinner />;
      }

    }
    else{
      return <Spinner />;
    }

    if (!instaposts) {
      return <Spinner />;
    }

    const childElements = instaposts.map((post, idx) => {
      if (post.embed_code !== "") {
        return (
          <div
            key={idx}
          // className="col-xl-4 col-lg-4 col-md-6 col-sm-12 grid-margin stretch-card"
          >
            <div dangerouslySetInnerHTML={this.createMarkup(post.embed_code)} />
          </div>
        );
      } else if (
        post.alt_google_photo_url !== "" &&
        post.alt_google_photo_url
      ) {
        return (
          <div
            key={idx}
          // className="col-xl-4 col-lg-4 col-md-6 col-sm-12 grid-margin img-responsive stretch-card"
          // style={{
          //   textAlign: "center",
          // }}
          >
            <a href={post.url} target="_blank" rel="noopener noreferrer">
              <img
                style={{
                  width: "80%",
                }}
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
    });

    return (
      <ResponsiveMasonry
        columnsCountBreakPoints={{ 350: 1, 750: 2, 900: 3 }}
      >
        <Masonry gutter={20}>{childElements}</Masonry>
      </ResponsiveMasonry>
    );

    // return (
    //   // <div className="row">
    //   //   <div className="col-10">
    //   <div
    //     className="row"
    //     style={{
    //       textAlign: "center",
    //     }}
    //   >
    //     {childElements}
    //   </div>
    //   //   </div>
    //   // </div>
    // );
  }
}
