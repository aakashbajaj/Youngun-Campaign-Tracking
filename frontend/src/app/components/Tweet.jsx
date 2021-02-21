import React from "react";
import {
  makeStyles,
  createMuiTheme,
  ThemeProvider,
} from "@material-ui/core/styles";
import clsx from "clsx";
import Card from "@material-ui/core/Card";
import CardHeader from "@material-ui/core/CardHeader";
// import CardMedia from "@material-ui/core/CardMedia";
import CardContent from "@material-ui/core/CardContent";
import CardActions from "@material-ui/core/CardActions";
import CardActionArea from "@material-ui/core/CardActionArea";
// import Collapse from "@material-ui/core/Collapse";
import Avatar from "@material-ui/core/Avatar";
import IconButton from "@material-ui/core/IconButton";
import Typography from "@material-ui/core/Typography";
import { red } from "@material-ui/core/colors";
// import FavoriteIcon from "@material-ui/icons/Favorite";
// import ShareIcon from "@material-ui/icons/Share";
// import ExpandMoreIcon from "@material-ui/icons/ExpandMore";
// import MoreVertIcon from "@material-ui/icons/MoreVert";
// import { SvgIcon, Icon } from "@material-ui/core";
// import ChatBubbleIcon from "@material-ui/icons/ChatBubble";
import RepeatIcon from "@material-ui/icons/Repeat";
import FavoriteBorderOutlinedIcon from "@material-ui/icons/FavoriteBorderOutlined";
import ChatBubbleOutlineRoundedIcon from "@material-ui/icons/ChatBubbleOutlineRounded";

// import instagram from "./instagram.svg";
// import logo from "./logo.svg";
// import twitter from "./twitter.svg";
import twitternew from "../../assets/images/twitternew.svg";
// import retweeticon from "./retweet2.svg";

// import { ReactComponent as RetweetIcon } from "./retweet2.svg";

// const theme = createMuiTheme({
//   typography: {
//     fontFamily: "Raleway, Arial",
//     marginLeft: "10%",
//   },
// });

const useStyles = makeStyles((theme) => ({
  root: {
    // maxWidth: 345,
  },
  media: {
    height: 0,
    paddingTop: "56.25%", // 16:9
  },
  imageIcon: {
    height: "100%",
  },
  expand: {
    transform: "rotate(0deg)",
    marginLeft: "auto",
    transition: theme.transitions.create("transform", {
      duration: theme.transitions.duration.shortest,
    }),
  },
  expandOpen: {
    transform: "rotate(180deg)",
  },
  avatar: {
    backgroundColor: red[500],
  },
  metric: {
    marginLeft: "12%",
  },
}));

function formatDateTime(string) {
  var options = {
    // year: "numeric",
    month: "short",
    day: "numeric",
    hour: "numeric",
    minute: "numeric",
  };
  return new Date(string).toLocaleDateString([], options);
}

function formatLargeNumeric(string) {
  var x = Number(string);
  var result = string;
  if (x > 1000000) {
    var num = (x / 1000000).toFixed(1);
    result = num.toString() + "M";
  } else if (x > 1000) {
    var num = (x / 1000).toFixed(1);
    result = num.toString() + "k";
  }

  return result;
}

function sanitCap(caption) {
  var lastidx = caption.lastIndexOf("https://");
  // console.log(lastidx);
  if (lastidx > 0) return caption.substring(0, lastidx);
  else return caption;
}

export default function Tweet(props) {
  const classes = useStyles();
  const [expanded, setExpanded] = React.useState(false);

  const handleExpandClick = () => {
    setExpanded(!expanded);
  };

  const routeTo = (tar_url) => {
    window.open(tar_url);
  };

  var hasMedia = false;
  // console.log(props.media_objs);
  if (props.media_objs) {
    if (props.media_objs.length > 0) {
      hasMedia = true;
    }
  }

  var profileURL = "https://twitter.com/" + props.account_username;
  var postURL = props.post_url;

  return (
    <Card className={classes.root}>
      <CardActionArea onClick={() => routeTo(profileURL)}>
        <CardHeader
          avatar={
            <Avatar
              aria-label="recipe"
              className={classes.avatar}
              src={props.profile_img_url}
            ></Avatar>
          }
          action={
            <IconButton href={profileURL}>
              <img
                className={classes.imageIcon}
                src={twitternew}
                alt="twitter logo"
              />
            </IconButton>
          }
          title={props.account_name}
          subheader={"@" + props.account_username}
        />
      </CardActionArea>
      <CardActionArea onClick={() => routeTo(postURL)}>
        <CardContent>
          <Typography
            fontFamily="Monospace"
            // variant="body2"
            // color="textSecondary"
            // component="p"
          >
            {sanitCap(props.caption)}
          </Typography>
        </CardContent>
        {hasMedia ? (
          <img
            className="card-img-top"
            src={props.media_objs[0].url}
            alt={props.account_username + " Media"}
          />
        ) : null}
        <IconButton
          disabled
          // className={clsx(classes.expand, {
          //   [classes.expandOpen]: expanded,
          // })}
          aria-label="uploaddate"
        >
          <Typography
            disabled
            variant="body2"
            color="textSecondary"
            component="p"
          >
            {formatDateTime(props.upload_date)}
          </Typography>
        </IconButton>
      </CardActionArea>
      <CardActions disableSpacing>
        <IconButton disabled aria-label="comments" style={{ color: "#1DA1F2" }}>
          <ChatBubbleOutlineRoundedIcon fontSize="small" />
          <Typography
            variant="body2"
            color="textSecondary"
            component="p"
            className={classes.metric}
          >
            {formatLargeNumeric(props.comment_cnt)}
          </Typography>
        </IconButton>
        <IconButton disabled aria-label="shares" style={{ color: "#47AF7B" }}>
          <RepeatIcon fontSize="small" />
          {/* <Icon style={{ color: "#47AF7B" }}>
            <img src={retweeticon} height={20} />
          </Icon> */}
          {/* <RetweetIcon style={{ color: "#47AF7B" }} /> */}
          <Typography
            variant="body2"
            color="textSecondary"
            component="p"
            className={classes.metric}
          >
            {formatLargeNumeric(props.retweet_cnt)}
          </Typography>
        </IconButton>
        <IconButton disabled aria-label="likes" style={{ color: "#E0245E" }}>
          <FavoriteBorderOutlinedIcon fontSize="small" />
          <Typography
            variant="body2"
            color="textSecondary"
            component="p"
            className={classes.metric}
          >
            {formatLargeNumeric(props.like_cnt)}
          </Typography>
        </IconButton>
        {/* <IconButton
          className={clsx(classes.expand, {
            [classes.expandOpen]: expanded,
          })}
          aria-label="show more"
        >
          <Typography variant="body2" color="textSecondary" component="p">
            {props.upload_date}
          </Typography>
        </IconButton> */}
      </CardActions>
    </Card>
  );
}
