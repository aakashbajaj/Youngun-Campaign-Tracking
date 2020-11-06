import React, { Component } from "react";
import PostListTable from "../components/PostListTable";

export default class PostStats extends Component {
  render() {
    return (
      <div className="row">
        <div className="col-12 grid-margin stretch-card">
          <PostListTable />
        </div>
      </div>
    );
  }
}
