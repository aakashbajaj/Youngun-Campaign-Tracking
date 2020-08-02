import React, { Component } from "react";
import CampaignContext from "../data/CampaignContext";
import Spinner from "../shared/Spinner";

// import ReactBricks from "react-bricks-infinite";

// import "./Masonry.css";

// import Masonry from "react-masonry-component";

// const masonryOptions = {
//   transitionDuration: 0,
//   columnWidth: 3,
// };

// const imagesLoadedOptions = { background: ".my-bg-image-el" };

const sizes = [
  { columns: 2, gutter: 20 },
  { mq: "768px", columns: 3, gutter: 25 },
  { mq: "1024px", columns: 5, gutter: 40 },
];

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
          <div
            key={idx}
            className="col-xl-4 col-lg-4 col-md-6 col-sm-12 grid-margin stretch-card"
          >
            <div dangerouslySetInnerHTML={this.createMarkup(post.embed_code)} />
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
    });

    return (
      // <div className="row">
      //   <div className="col-10">
      <div className="row">{childElements}</div>
      //   </div>
      // </div>
    );
  }
}
