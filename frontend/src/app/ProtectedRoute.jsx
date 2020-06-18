import React from "react";
import { Route, Redirect } from "react-router-dom";
import CampaignContext from "./data/CampaignContext";

export const ProtectedRoute = ({ component: Component, ...rest }) => {
  return (
    <CampaignContext.Consumer>
      {({ isAuthenticated }) => (
        <Route
          {...rest}
          render={(props) => {
            if (isAuthenticated) {
              return <Component {...props} />;
            } else {
              return (
                <Redirect
                  to={{
                    pathname: "/login",
                    state: {
                      from: props.location,
                    },
                  }}
                />
              );
            }
          }}
        />
      )}
    </CampaignContext.Consumer>
  );
};
