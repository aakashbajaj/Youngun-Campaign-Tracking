import React, {
  Component,
  useContext,
  useEffect,
  useLayoutEffect,
} from "react";
import CampaignContext from "../data/CampaignContext";
import Spinner from "../shared/Spinner";

import Colcade from "colcade";
import { makeStyles } from "@material-ui/core/styles";

const useStyles = makeStyles((theme) => ({
  grid: {
    display: "flex",
    marginTop: theme.spacing(4),
  },
  grid_col: {
    flexGrow: 1,
    paddingLeft: theme.spacing(2),
    paddingRight: theme.spacing(2),
  },
  grid_item: {
    paddingBottom: theme.spacing(3),
  },
  grid_col_1: {},
  grid_col_2: { display: "none" },
  grid_col_3: { display: "none" },
  [theme.breakpoints.up("sm")]: {
    grid_col_2: { display: "block" },
  },
  [theme.breakpoints.up("md")]: {
    grid_col_3: { display: "block" },
  },
}));

const InstaFeedFunc = (props) => {
  const classes = useStyles();
  const gContext = useContext(CampaignContext);

  const createMarkup = (embed_code) => {
    return { __html: embed_code };
  };

  useEffect(() => {
    window.instgrm.Embeds.process();
  });

  useLayoutEffect(() => {
    const colc = new Colcade(`.${classes.grid}`, {
      columns: `.${classes.grid_col}`,
      items: `.${classes.grid_item}`,
    });
    window.instgrm.Embeds.process();
  });

  const childElements = gContext.liveCampaignFeed[
    gContext.currentCampaignInView
  ].instagram.map((post, idx) => {
    if (post.embed_code !== "") {
      return (
        <div key={idx} className={classes.grid_item}>
          <div dangerouslySetInnerHTML={createMarkup(post.embed_code)} />
        </div>
      );
    } else if (
      post.alt_google_photo_url !== "" &&
      post.alt_google_photo_url !== null
    ) {
      return (
        <div key={idx} className={classes.grid_item}>
          <a href={post.url} target="_blank" rel="noopener noreferrer">
            <img
              style={{
                width: "80%",
              }}
              key={post.alt_google_photo_url}
              src={post.alt_google_photo_url}
              alt={"Post"}
              loader={<Spinner />}
            />
          </a>
        </div>
      );
    }
    return null;
  });

  return (
    <div className={classes.grid}>
      <div className={`${classes.grid_col} ${classes.grid_col_1}`}></div>
      <div className={`${classes.grid_col} ${classes.grid_col_2}`}></div>
      <div className={`${classes.grid_col} ${classes.grid_col_3}`}></div>
      {childElements}
    </div>
  );
};

export default InstaFeedFunc;
