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

const createMarkup = (embed_code) => {
  return { __html: embed_code };
};

const postLoader = (posts, itemClass, page) => {
  return posts.map((post, idx) => {
    if (post.embed_code !== "") {
      return (
        <div key={idx} className={`${itemClass} page-${page}-item`}>
          <div dangerouslySetInnerHTML={createMarkup(post.embed_code)} />
        </div>
      );
    } else if (
      post.alt_google_photo_url !== "" &&
      post.alt_google_photo_url !== null
    ) {
      return (
        <div key={idx} className={`${itemClass} page-${page}-item`}>
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

const TwitterFeedTrial = (props) => {
  const classes = useStyles();
  const gContext = useContext(CampaignContext);

  const [hasMore, setHasMore] = useState(true);

  const initPostRender = postLoader(
    gContext.liveCampaignFeed[gContext.currentCampaignInView].twitter.slice(
      0,
      9
    ),
    classes.grid_item,
    1
  );
  const [displayPosts, setDisplayPosts] = useState(initPostRender);
  const [page, setPage] = useState(1);
  const [allPosts, setAllPosts] = useState([]);
  const [colcGrid, setColcGrid] = useState(null);

  const loader = useRef(null);

  const handleObserver = (entities) => {
    const target = entities[0];
    if (target.isIntersecting) {
      setPage((page) => page + 1);
    }
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

  useLayoutEffect(() => {
    const colc = new Colcade(`.${classes.grid}`, {
      columns: `.${classes.grid_col}`,
      items: `.${classes.grid_item}`,
    });
    setColcGrid(colc);
    window.twttr.widgets.load();
  });

  useEffect(() => {
    var currPostCount = displayPosts.length;
    const addPostsRender = postLoader(
      gContext.liveCampaignFeed[gContext.currentCampaignInView].twitter.slice(
        currPostCount,
        currPostCount + 9
      ),
      classes.grid_item,
      page
    );
    setDisplayPosts(displayPosts.concat(addPostsRender));
  }, [page]);

  useEffect(() => {
    var currPostCount = displayPosts.length;
    if (
      currPostCount >=
      gContext.liveCampaignFeed[gContext.currentCampaignInView].twitter.length
    ) {
      setHasMore(false);
    }
    console.log(document.getElementsByClassName(`${classes.grid_item}`));
    console.log(colcGrid);
    if (colcGrid !== null) {
      colcGrid.append(document.getElementsByClassName(`page-${page}-item`));
    }
    window.twttr.widgets.load();
  }, [displayPosts]);

  // useEffect(() => {
  //   const colc = new Colcade(`.${classes.grid}`, {
  //     columns: `.${classes.grid_col}`,
  //     items: `.${classes.grid_item}`,
  //   });
  //   setColcGrid(colc);
  //   console.log(displayPosts.length);
  //   console.log(displayPosts);
  //   console.log(postLoader(displayPosts));
  //   colc.append(document.getElementsByClassName(`.${classes.grid_item}`));
  //   window.twttr.widgets.load();
  // }, []);

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
        {displayPosts}
      </div>
      <div className="loading" ref={loader}>
        <h2>Load More...</h2>
      </div>
    </div>
  );
};

export default TwitterFeedTrial;
