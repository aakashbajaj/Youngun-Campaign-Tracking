import React, { Component } from "react";
import CampaignContext from "../data/CampaignContext";
import Spinner from "../shared/Spinner";

const ListItem = (props) => {
  return (
    <li>
      {/* <li className={props.isCompleted ? "completed" : null}> */}
      <div className="form-check form-check-success m-0 align-items-start">
        <label htmlFor="" className="form-check-label font-weight-medium">
          {/* <input
            className="checkbox"
            type="checkbox"
            checked={props.isCompleted}
            onChange={props.changed}
          />{" "} */}
          {props.children} <i className="input-helper"></i>
        </label>
      </div>
      <i
        className="remove mdi mdi-close-circle-outline"
        onClick={props.remove}
      ></i>
    </li>
  );
};

export default class InviteUserCard extends Component {
  static contextType = CampaignContext;

  state = {
    inputEmail: "",
  };

  inputChangeHandler = (evt) => {
    evt.preventDefault();
    this.setState({
      inputEmail: evt.target.value,
    });
  };

  inviteEmailUser = (evt) => {
    evt.preventDefault();
    this.context.inviteEmailUser(this.state.inputEmail);
  };

  removeInvitedUser = (email) => {
    if (window.confirm(`Remove ${email} ?`)) {
      this.context.removeInvitedUser(email);
    }
  };

  render() {
    var invited_profiles = [];
    if (this.context.invited_profiles) {
      if (this.context.invited_profiles[this.context.currentCampaignInView]) {
        invited_profiles = this.context.invited_profiles[
          this.context.currentCampaignInView
        ];
      }
    }
    if (!invited_profiles) {
      return <Spinner />;
    }
    return (
      <div className="card">
        <div className="card-body">
          <h4 className="card-title">Invite Team Members</h4>
          <form className="add-items d-lg-flex" onSubmit={this.inviteEmailUser}>
            <input
              type="text"
              className="form-control h-auto"
              placeholder="Enter Official Email ID"
              value={this.state.inputEmail}
              onChange={this.inputChangeHandler}
              required
            />
            <button
              type="submit"
              className="btn btn-primary font-weight-bold ml-0 mt-2 mt-lg-0"
            >
              Add
            </button>
          </form>
          <div className="list-wrapper">
            <ul className="d-flex flex-column todo-list todo-padding-lg">
              {invited_profiles.map((profile, index) => {
                return (
                  <ListItem
                    key={profile.email}
                    remove={() => this.removeInvitedUser(profile.email)}
                  >
                    {profile.email}
                  </ListItem>
                );
              })}
            </ul>
          </div>
        </div>
      </div>
    );
  }
}
