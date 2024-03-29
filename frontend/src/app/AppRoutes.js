import React, { Component, Suspense, lazy } from "react";
import { Switch, Route, Redirect } from "react-router-dom";
import Spinner from "./shared/Spinner";
import { ProtectedRoute } from "./ProtectedRoute";

// const Buttons = lazy(() => import("./basic-ui/Buttons"));
// const Dropdowns = lazy(() => import("./basic-ui/Dropdowns"));
// const Typography = lazy(() => import("./basic-ui/Typography"));

// const BasicElements = lazy(() => import("./form-elements/BasicElements"));

// const BasicTable = lazy(() => import("./tables/BasicTable"));

// const FontAwesome = lazy(() => import("./icons/FontAwesome"));

// const ChartJs = lazy(() => import("./charts/ChartJs"));

// const Error500 = lazy(() => import("./user-pages/Error500"));

// const BlankPage = lazy(() => import("./user-pages/BlankPage"));

const Dashboard = lazy(() => import("./pages/Dashboard"));
const Reporting = lazy(() => import("./pages/Reporting"));
const PostStats = lazy(() => import("./pages/PostStats"));
const Login = lazy(() => import("./pages/Login/Login"));
const VerifyOtp = lazy(() => import("./pages/Login/VerifyOtp"));
const Error404 = lazy(() => import("./shared/Error404"));
const StoriesFeed = lazy(() => import("./pages/Feeds/StoriesFeed"));
const PostsFeed = lazy(() => import("./pages/Feeds/PostsFeed"));

class AppRoutes extends Component {
  render() {
    return (
      <Suspense fallback={<Spinner />}>
        <Switch>
          <ProtectedRoute exact path="/" component={Dashboard} />

          <Route exact path="/login" component={Login} />
          <Route exact path="/verify" component={VerifyOtp} />
          <ProtectedRoute exact path="/storiesfeed" component={StoriesFeed} />
          <ProtectedRoute exact path="/postsfeed" component={PostsFeed} />
          <ProtectedRoute exact path="/report/post-stats" component={PostStats} />
          <ProtectedRoute exact path="/report/overview" component={Reporting} />

          <ProtectedRoute path="/404" component={Error404} />

          {/* <Route path="/basic-ui/buttons" component={Buttons} />
          <Route path="/basic-ui/dropdowns" component={Dropdowns} />
          <Route path="/basic-ui/typography" component={Typography} />

          <Route
            path="/form-Elements/basic-elements"
            component={BasicElements}
          />

          <Route path="/tables/basic-table" component={BasicTable} />

          <Route path="/icons/font-awesome" component={FontAwesome} />

          <Route path="/charts/chart-js" component={ChartJs} />

          <Route path="/user-pages/error-404" component={Error404} />
          <Route path="/user-pages/error-500" component={Error500} />

          <Route path="/user-pages/blank-page" component={BlankPage} /> */}

          <Redirect to="/404" />
        </Switch>
      </Suspense>
    );
  }
}

export default AppRoutes;
