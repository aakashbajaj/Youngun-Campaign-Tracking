import axios from "axios";

// const API = {
//   setAuthTokenHeader: (token) => {
//     if (token) {
//       console.log(`setting token ${token}`);
//       axios.defaults.headers.common["Authorization"] = `Token ${token}`;
//     } else {
//       axios.defaults.headers.common["Authorization"] = null;
//       /*if setting null does not remove `Authorization` header then try
//              delete axios.defaults.headers.common['Authorization'];
//            */
//     }
//   },

//   agent: axios.create({
//     baseURL: "http://localhost:8000/",
//   }),
// };

// export default API;

console.log(process.env.REACT_APP_BACKENDURL);
const API = axios.create({
  baseURL: "https://trackingapi.youngun.in/",
});

export const setAuthTokenHeader = (token) => {
  if (token) API.defaults.headers.common["Authorization"] = `Token ${token}`;
  else API.defaults.headers.common["Authorization"] = null;
};

export default API;
