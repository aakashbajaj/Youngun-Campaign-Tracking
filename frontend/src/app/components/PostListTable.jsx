import React, { Component } from "react";
import CampaignContext from "../data/CampaignContext";
import Spinner from "../shared/Spinner";

export default class PostListTable extends Component {
  static contextType = CampaignContext;

  render() {
    var postsList = [];
    if (this.context.currentCampaignInView === null || postsList === []) {
      return <Spinner />;
    }
    if (this.context.currentCampaignInView) {
      if (this.context.campaignReportData) {
        if (
          this.context.campaignReportData[this.context.currentCampaignInView]
        ) {
          if (
            this.context.campaignReportData[this.context.currentCampaignInView]
              .posts
          ) {
            postsList = this.context.campaignReportData[
              this.context.currentCampaignInView
            ].posts;
          }
        }
      }
    }

    const childElements = postsList.map((post, idx) => {
      const options = {
        day: "numeric",
        month: "long",
      };
      console.log(post);
      console.log(
        new Date(post.upload_date).toLocaleDateString(undefined, options)
      );
      return (
        <tr key={idx}>
          <td>{idx + 1}</td>
          <td>
            {new Date(post.upload_date).toLocaleDateString(undefined, options)}
          </td>
          <td>
            <a href={post.url} target="_blank" rel="noopener noreferrer">
              {post.url}
            </a>
          </td>
          {post.likes ? <td>{post.likes}</td> : <td>-</td>}
          {post.comments ? <td>{post.comments}</td> : <td>-</td>}
          {post.post_shares ? <td>{post.post_shares}</td> : <td>-</td>}
          {/* {post.post_saves ? <td>{post.post_saves}</td> : <td>-</td>}
          {post.post_engagement ? <td>{post.post_engagement}</td> : <td>-</td>}
          {post.post_reach ? <td>{post.post_reach}</td> : <td>-</td>}
          {post.total_views ? <td>{post.total_views}</td> : <td>-</td>} */}
        </tr>
      );
    });

    console.log(postsList);

    return (
      <div className="card">
        <div className="card-body">
          <h4 className="card-title">Post Statistics</h4>
          <p className="card-description"> Detailed engagement of each post</p>
          <div className="table-responsive">
            <table className="table table-hover table-striped">
              <thead>
                <tr>
                  <th>S.No.</th>
                  <th>TimeStamp</th>
                  <th>Post Link</th>
                  <th>Likes</th>
                  <th>Comments</th>
                  <th>
                    Post Shares /<br />
                    ReTweets
                  </th>
                  {/* <th>
                    Post Saves <br />
                    (Instagram)
                  </th>
                  <th>
                    Total Media <br />
                    Engagement
                  </th>
                  <th>Static Post Reach</th>
                  <th>Video Views</th> */}
                </tr>
              </thead>
              <tbody>{childElements}</tbody>
            </table>
          </div>
        </div>
      </div>
    );
  }
}
