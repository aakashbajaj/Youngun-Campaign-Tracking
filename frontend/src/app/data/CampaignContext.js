import React from "react";

export default React.createContext({
  user: null,
  userEmail: null,
  isAuthenticated: false,
  isAuthInProgress: false,
  errors: {},
  campaigns: {},
  liveCampaignData: {},
  liveCampaignFeed: {},
  campaignReportData: {},

  login: () => {},
  logout: () => {},
  verify: () => {},

  initiateLogin: () => {},
});
