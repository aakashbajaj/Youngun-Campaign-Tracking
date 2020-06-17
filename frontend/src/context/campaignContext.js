import React from "react";

export default React.createContext({
  user: null,
  authDetails: null,
  isAuthenticated: false,
  isAuthInProgress: false,
  errors: [],
  campaigns: [],
  liveCampaignData: {},
  campaignReportData: {},

  login: () => {},
  logout: () => {},
  verify: () => {},
});
