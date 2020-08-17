import React, {
  Component,
  useContext,
  useEffect,
  useLayoutEffect,
  useRef,
  useState,
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
    // paddingLeft: theme.spacing(2),
    // paddingRight: theme.spacing(2),
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

const TwitterFeed = (props) => {
  const classes = useStyles();
  const gContext = useContext(CampaignContext);

  const [hasMore, setHasMore] = useState(true);
  const [displayPosts, setDisplayPosts] = useState(
    gContext.liveCampaignFeed[gContext.currentCampaignInView].twitter.slice(
      0,
      9
    )
  );
  const [page, setPage] = useState(1);
  const [allPosts, setAllPosts] = useState([]);
  const [colcGrid, setColcGrid] = useState(null);

  const createMarkup = (embed_code) => {
    return { __html: embed_code };
  };

  const loader = useRef(null);

  const handleObserver = (entities) => {
    const target = entities[0];
    if (target.isIntersecting) {
      setPage((page) => page + 1);
    }
  };

  const postLoader = (posts) => {
    return posts.map((post, idx) => {
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
  };

  useEffect(() => {
    var options = {
      root: null,
      rootMargin: "20px",
      threshold: 1.0,
    };
    const observer = new IntersectionObserver(handleObserver, options);
    if (loader.current) {
      observer.observe(loader.current);
    }
  }, []);

  useEffect(() => {
    var currPostCount = displayPosts.length;
    setDisplayPosts(
      displayPosts.concat(
        gContext.liveCampaignFeed[gContext.currentCampaignInView].twitter.slice(
          currPostCount,
          currPostCount + 9
        )
      )
    );
  }, [page]);

  useEffect(() => {
    var currPostCount = displayPosts.length;
    if (
      currPostCount >=
      gContext.liveCampaignFeed[gContext.currentCampaignInView].twitter.length
    ) {
      setHasMore(false);
    }
  }, [displayPosts, gContext.liveCampaignFeed]);

  useEffect(() => {
    console.log(document.getElementsByClassName(`${classes.grid_item}`));
    if (colcGrid !== null) {
      colcGrid.append(document.getElementsByClassName(`${classes.grid_item}`));
    }
    window.twttr.widgets.load();
  });

  // useLayoutEffect(() => {
  //   const colc = new Colcade(`.${classes.grid}`, {
  //     columns: `.${classes.grid_col}`,
  //     items: `.${classes.grid_item}`,
  //   });
  //   window.twttr.widgets.load();
  // });

  useEffect(() => {
    const colc = new Colcade(`.${classes.grid}`, {
      columns: `.${classes.grid_col}`,
      items: `.${classes.grid_item}`,
    });
    setColcGrid(colc);
    console.log(displayPosts.length);
    console.log(displayPosts);
    console.log(postLoader(displayPosts));
    colc.append(document.getElementsByClassName(`.${classes.grid_item}`));
    window.twttr.widgets.load();
  }, []);

  // const childElements = displayPosts.map((post, idx) => {
  //   if (post.embed_code !== "") {
  //     return (
  //       <div key={idx} className={classes.grid_item}>
  //         <div dangerouslySetInnerHTML={createMarkup(post.embed_code)} />
  //       </div>
  //     );
  //   } else if (
  //     post.alt_google_photo_url !== "" &&
  //     post.alt_google_photo_url !== null
  //   ) {
  //     return (
  //       <div key={idx} className={classes.grid_item}>
  //         <a href={post.url} target="_blank" rel="noopener noreferrer">
  //           <img
  //             style={{
  //               width: "80%",
  //             }}
  //             key={post.alt_google_photo_url}
  //             src={post.alt_google_photo_url}
  //             alt={"Post"}
  //             loader={<Spinner />}
  //           />
  //         </a>
  //       </div>
  //     );
  //   }
  //   return null;
  // });

  if (displayPosts === []) {
    return <Spinner />;
  }

  return (
    <div>
      <div className={`${classes.grid} row`}>
        <div
          className={`${classes.grid_col} ${classes.grid_col_1} col-sm-12 col-md-6 col-lg-4`}
        ></div>
        <div
          className={`${classes.grid_col} ${classes.grid_col_2} col-md-6 col-lg-4`}
        ></div>
        <div
          className={`${classes.grid_col} ${classes.grid_col_3} col-lg-4`}
        ></div>
        {postLoader(displayPosts)}
      </div>
      <div className="loading" ref={loader}>
        <h2>Load More...</h2>
      </div>
    </div>
  );
};

export default TwitterFeed;
