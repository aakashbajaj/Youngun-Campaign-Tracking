import React, { Component } from "react";
import CampaignContext from "../../data/CampaignContext";
import Spinner from "../../shared/Spinner";

import Masonry, { ResponsiveMasonry } from "react-responsive-masonry";

// import InfiniteScroll from "react-infinite-scroll-component";
// import Tweet from "../../components/Tweet";

import TweetEmbed from 'react-tweet-embed'

export default class TwitterFeed extends Component {
  static contextType = CampaignContext;

  createMarkup(embed_code) {
    return { __html: embed_code };
  }

  state = {
    allTwitterPosts: [],
    displayTwitterPosts: [],
    hasMore: true,
  };

  // showMorePosts = () => {
  //   var currPostCount = this.state.displayTwitterPosts.length;

  //   if (
  //     currPostCount >=
  //     this.context.liveCampaignFeed[this.context.currentCampaignInView].twitter
  //       .length
  //   ) {
  //     this.setState({ hasMore: false });
  //   }
  //   this.setState({
  //     displayTwitterPosts: this.state.displayTwitterPosts.concat(
  //       this.context.liveCampaignFeed[
  //         this.context.currentCampaignInView
  //       ].twitter.slice(currPostCount, currPostCount + 9)
  //     ),
  //   });
  //   window.twttr.widgets.load();
  // };

  componentDidMount() {
    // console.log("in TW CDM");
    // window.twttr.widgets.load();

    // this.setState({
    //   displayTwitterPosts: this.context.liveCampaignFeed[
    //     this.context.currentCampaignInView
    //   ].twitter.slice(0, 9),
    // });
  }

  componentDidUpdate(prevProps, prevState) {
    // window.twttr.widgets.load();
  }

  render() {
    var twitterposts = [];
    if (
      this.context.currentCampaignInView &&
      this.context.liveCampaignFeed[this.context.currentCampaignInView]
    ) {

      if (this.context.liveCampaignFeed[this.context.currentCampaignInView]
        .twitter) {

        twitterposts = this.context.liveCampaignFeed[
          this.context.currentCampaignInView
        ].twitter;
      }

      else {
        return <Spinner />;
      }

    }

    else {
      return <Spinner />;
    }

    // var postsOnPage = this.state.displayTwitterPosts.map((post, idx) => {
    //   if (post.embed_code !== "") {
    //     return (
    //       <div key={idx}>
    //         <div
    //           className="col-xl-4 col-lg-4 col-md-6 col-sm-12 grid-margin stretch-card"
    //           dangerouslySetInnerHTML={this.createMarkup(post.embed_code)}
    //         />
    //       </div>
    //     );
    //   } else if (
    //     post.alt_google_photo_url !== "" &&
    //     post.alt_google_photo_url !== null
    //   ) {
    //     return (
    //       <div
    //         key={idx}
    //         className="col-xl-4 col-lg-4 col-md-6 col-sm-12 grid-margin stretch-card"
    //       >
    //         <a href={post.url} target="_blank" rel="noopener noreferrer">
    //           <img
    //             key={post.alt_google_photo_url}
    //             src={post.alt_google_photo_url}
    //             alt={"Post"}
    //             loader={<Spinner />}
    //           />
    //         </a>
    //       </div>
    //     );
    //   }
    //   return null;
    // });

    var postsOnPage = twitterposts.map((post, idx) => {
      if (post.embed_code !== "") {

        var matches = post.url.match(/\d+$/);

        if (matches) {
          var post_id = matches[0];
          return (
            <div key={idx}>
              <TweetEmbed id={post_id} />
            </div>
          );
        } else {
          return null;
        }

        // return (
        //   <div key={idx}>
        //     <Tweet
        //       post_url={post.url}
        //       profile_img_url={post.prof_img_url}
        //       account_name={post.account_name}
        //       account_username={post.post_username}
        //       caption={post.caption}
        //       comment_cnt={post.comments}
        //       retweet_cnt={post.post_shares}
        //       like_cnt={post.likes}
        //       upload_date={post.upload_date}
        //       media_objs={post.media_objs}
        //     />
        //   </div>
        // );
      } else if (
        post.alt_google_photo_url !== "" &&
        post.alt_google_photo_url !== null
      ) {
        return (
          <div key={idx}>
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
    });

    if (!twitterposts || twitterposts.length === 0) {
      return <Spinner />;
    }

    // if (
    //   !this.state.displayTwitterPosts ||
    //   this.state.displayTwitterPosts.length === 0
    // ) {
    //   return <Spinner />;
    // }

    return (
      <ResponsiveMasonry
        columnsCountBreakPoints={{ 350: 1, 750: 2, 900: 3 }}
      >
        <Masonry gutter={20}>{postsOnPage}</Masonry>
      </ResponsiveMasonry>
    );

    // return (
    //   <div>
    //     <InfiniteScroll
    //       dataLength={this.state.displayTwitterPosts.length}
    //       next={this.showMorePosts}
    //       hasMore={this.state.hasMore}
    //       loader={<h4>Loading...</h4>}
    //       endMessage={
    //         <p style={{ textAlign: "center" }}>
    //           <b>You have seen it all</b>
    //         </p>
    //       }
    //     >
    //       <div className="row">{postsOnPage}</div>
    //     </InfiniteScroll>
    //   </div>
    // );
  }
}
