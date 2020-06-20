import React, { Component } from "react";
import { Bar } from "react-chartjs-2";

import CampaignContext from "../data/CampaignContext";
import StoryMetric from "../components/StoryMetric";
import CardDoughnut from "../components/CardDoughnut";
import Spinner from "../shared/Spinner";
import ContentSlideCard from "../components/ContentSlideCard";
// import DatePicker from 'react-datepicker';
// import { Dropdown } from 'react-bootstrap';

export class Dashboard extends Component {
  static contextType = CampaignContext;

  currentCampLiveMetricsTemp = {
    name: "",
    organisation: {
      name: "",
    },
    hashtag: "",
    status: "",

    start_date: "",
    end_date: "",

    slide_url: "",
    live_google_sheet: "",
    slug: "",

    particaipating_profiles: "",
    unique_content_pieces: "",
    approved_content_pieces: "",
    remaining_content_pieces: "",

    last_updated: "",

    fb_posts: "",
    fb_stories: "",

    in_posts: "",
    in_stories: "",

    tw_posts: "",
    tw_stories: "",

    live_fb_posts: "",
    live_fb_stories: "",

    live_in_posts: "",
    live_in_stories: "",

    live_tw_posts: "",
    live_tw_stories: "",
  };

  state = {
    currentCampaign: null,
  };

  constructor(props) {
    super(props);

    this.statusChangedHandler = this.statusChangedHandler.bind(this);
    this.inputChangeHandler = this.inputChangeHandler.bind(this);
  }
  componentDidMount() {
    this.setState({ currentCampaign: this.context.currentCampaignInView });

    // const liveCampMetrics = this.context.liveCampaignData[
    //   this.context.currentCampaignInView
    // ];
    // this.setState({ currentCampLiveMetrics: liveCampMetrics });
  }

  statusChangedHandler(event, id) {
    const todo = { ...this.state.todos[id] };
    todo.isCompleted = event.target.checked;

    const todos = [...this.state.todos];
    todos[id] = todo;

    this.setState({
      todos: todos,
    });
  }

  inputChangeHandler(event) {
    this.setState({
      inputValue: event.target.value,
    });
  }
  areaData = {
    labels: ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"],
    datasets: [
      {
        label: "Product-1",
        data: [3, 3, 8, 5, 7, 4, 6, 4, 6, 3],
        backgroundColor: "#2196f3",
        borderColor: "#0c83e2",
        borderWidth: 1,
        fill: true,
        datasetKeyProvider: "key1",
      },
      {
        label: "Product-2",
        data: [7, 5, 14, 7, 12, 6, 10, 6, 11, 5],
        backgroundColor: "#19d895",
        borderColor: "#15b67d",
        borderWidth: 1,
        fill: true,
        datasetKeyProvider: "key2",
      },
    ],
  };

  areaOptions = {
    responsive: true,
    maintainAspectRatio: true,
    scales: {
      yAxes: [
        {
          gridLines: {
            color: "#F2F6F9",
          },
          ticks: {
            beginAtZero: true,
            min: 0,
            max: 20,
            stepSize: 5,
          },
        },
      ],
      xAxes: [
        {
          gridLines: {
            color: "#F2F6F9",
          },
          ticks: {
            beginAtZero: true,
          },
        },
      ],
    },
    legend: {
      display: false,
    },
    elements: {
      point: {
        radius: 2,
      },
    },
    layout: {
      padding: {
        left: 0,
        right: 0,
        top: 0,
        bottom: 0,
      },
    },
    stepsize: 1,
  };

  amountDueBarData = {
    labels: [
      "Day 1",
      "Day 2",
      "Day 3",
      "Day 4",
      "Day 5",
      "Day 6",
      "Day 7",
      "Day 8",
      "Day 9",
      "Day 10",
    ],
    datasets: [
      {
        label: "Profit",
        data: [39, 19, 25, 16, 31, 39, 12, 18, 33, 24],
        backgroundColor: [
          "#2196f3",
          "#2196f3",
          "#2196f3",
          "#2196f3",
          "#2196f3",
          "#2196f3",
          "#2196f3",
          "#2196f3",
          "#2196f3",
          "#2196f3",
        ],
        borderColor: [
          "#2196f3",
          "#2196f3",
          "#2196f3",
          "#2196f3",
          "#2196f3",
          "#2196f3",
          "#2196f3",
          "#2196f3",
          "#2196f3",
          "#2196f3",
        ],
        borderWidth: 2,
        fill: true,
      },
    ],
  };

  amountDueBarOptions = {
    layout: {
      padding: {
        left: 0,
        right: 0,
        top: 0,
        bottom: 0,
      },
    },

    scales: {
      responsive: true,
      maintainAspectRatio: true,
      yAxes: [
        {
          display: false,
          gridLines: {
            color: "rgba(0, 0, 0, 0.03)",
          },
        },
      ],
      xAxes: [
        {
          display: false,
          barPercentage: 0.4,
          gridLines: {
            display: false,
          },
        },
      ],
    },
    legend: {
      display: false,
    },
  };
  toggleProBanner() {
    document.querySelector(".proBanner").classList.toggle("hide");
  }

  render() {
    var liveCampMetrics = this.currentCampLiveMetrics;
    if (
      this.context.currentCampaignInView !== null &&
      this.context.liveCampaignData[this.context.currentCampaignInView] !== null
    ) {
      liveCampMetrics = this.context.liveCampaignData[
        this.context.currentCampaignInView
      ];
    } else {
      liveCampMetrics = this.currentCampLiveMetrics;
    }
    console.log(liveCampMetrics);
    if (!liveCampMetrics) {
      return <Spinner />;
    }
    return (
      <div>
        <div className="page-header">
          <h3 className="page-title">
            {liveCampMetrics && liveCampMetrics.organisation
              ? liveCampMetrics.organisation.name
              : null}
          </h3>
          <nav aria-label="breadcrumb">
            <ol className="breadcrumb">
              <li className="breadcrumb-item">
                {liveCampMetrics ? (
                  <a
                    href={`https://www.instagram.com/explore/tags/${liveCampMetrics.hashtag}/`}
                    target="_blank"
                    rel="noopener noreferrer"
                    // onClick={(event) => event.preventDefault()}
                  >
                    #{liveCampMetrics.hashtag}
                  </a>
                ) : null}
              </li>
            </ol>
          </nav>
        </div>
        <div className="row">
          <div className="col-xl-4 col-lg-6 col-md-6 col-sm-6 grid-margin stretch-card">
            {/* Instagram */}
            <StoryMetric
              platform="in"
              mainText={`Posts Live: ${liveCampMetrics.live_in_posts}`}
              subText={`Total Posts: ${liveCampMetrics.in_posts}`}
            />
          </div>
          <div className="col-xl-4 col-lg-6 col-md-6 col-sm-6 grid-margin stretch-card">
            {/* Facebook */}
            <StoryMetric
              platform="fb"
              mainText={`Posts Live: ${liveCampMetrics.live_fb_posts}`}
              subText={`Total Posts: ${liveCampMetrics.fb_posts}`}
            />
          </div>
          <div className="col-xl-4 col-lg-6 col-md-6 col-sm-6 grid-margin stretch-card">
            {/* Twitter */}
            <StoryMetric
              platform="tw"
              mainText={`Posts Live: ${liveCampMetrics.live_tw_posts}`}
              subText={`Total Posts: ${liveCampMetrics.tw_posts}`}
            />
          </div>
          {/* <div className="col-xl-4 col-lg-6 col-md-6 col-sm-6 grid-margin stretch-card">
            C4
            <StoryMetric
              platform="tw"
              mainText={liveCampMetrics.name}
              subText="QWER"
            />
          </div> */}
        </div>
        {/* <div className="row">
          <div className="col-xl-4 col-lg-6 col-sm-6  grid-margin stretch-card">
            C5
          </div>
          <div className="col-xl-4 col-lg-6 col-sm-6 grid-margin stretch-card">
            CC
          </div>
          <div className="col-xl-4 col-lg-12 col-sm-12 grid-margin stretch-card">
            <div className="row flex-grow">
              <div className="col-xl-12 col-lg-6 col-sm-6 grid-margin-0 grid-margin-xl stretch-card">
                CC
              </div>
              <div className="col-xl-12 col-lg-6 col-sm-6 stretch-card">
                CC
              </div>
            </div>
          </div>
        </div> */}
        <div className="row">
          <div className="col-sm-6 col-md-6 col-lg-6 grid-margin stretch-card">
            <CardDoughnut
              unique_content_pieces={liveCampMetrics.unique_content_pieces}
              approved_content_pieces={liveCampMetrics.approved_content_pieces}
              remaining_content_pieces={
                liveCampMetrics.remaining_content_pieces
              }
            />
          </div>
          <div className="col-sm-6 col-md-6 col-lg-6 grid-margin stretch-card">
            <div className="card card-statistics">
              <div className="card-body">
                <div className="clearfix">
                  <div className="float-left">
                    <i className="mdi mdi-receipt text-warning icon-lg"></i>
                  </div>
                  <div className="float-right">
                    <p className="mb-0 text-right text-dark"></p>
                    <div className="fluid-container">
                      <h3 className="font-weight-medium text-right mb-0 mt-3 text-dark">
                        <a
                          href={`${liveCampMetrics.slide_url}`}
                          target="_blank"
                          rel="noopener noreferrer"
                        >
                          View Content Slide
                        </a>
                      </h3>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    );
  }
}
export default Dashboard;
