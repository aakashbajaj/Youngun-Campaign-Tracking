import { toast } from "react-toastify";

//#region Notify Toasts
const Notify = {
  notifyError: (msg) => {
    console.log(msg);
    toast.error(msg, {
      position: "bottom-right",
      autoClose: 5000,
      hideProgressBar: true,
      closeOnClick: true,
      pauseOnHover: true,
      draggable: true,
      progress: undefined,
    });
  },

  notifyWarning: (msg) => {
    console.log(msg);
    toast.warning(msg, {
      position: "bottom-right",
      autoClose: 5000,
      hideProgressBar: true,
      closeOnClick: true,
      pauseOnHover: true,
      draggable: true,
      progress: undefined,
    });
  },

  notifyInfo: (msg) => {
    console.log(msg);
    toast.info(msg, {
      position: "bottom-left",
      autoClose: 5000,
      hideProgressBar: true,
      closeOnClick: true,
      pauseOnHover: true,
      draggable: true,
      progress: undefined,
    });
  },
};

export default Notify;
//#endregion
