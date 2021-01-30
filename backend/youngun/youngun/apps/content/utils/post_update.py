from pprint import pprint
from datetime import datetime
import math
import dateutil
import pytz

from youngun.apps.content.helpers.graphapi.igmedia import get_ig_media_data

from youngun.apps.content.helpers import in_post, fb_post, tw_post
from youngun.apps.content.models import InstagramPost, FacebookPost, TwitterPost, Post, Media


def tw_post_updater(post_pk):
    post = TwitterPost.objects.get(pk=post_pk)
    data = tw_post.get_tw_post_details(post.url)

    pprint(data)
    print(data["error"])

    if data["error"] is None:
        data = data["result"]

        post.alive = True
        post.likes = data["likes"]
        post.comments = data["comments"]
        post.post_username = data["username"]
        post.caption = data["caption"]
        post.upload_date = datetime.strptime(
            data["timestamp"], "%Y-%m-%d %H:%M:%S")
        post.account_name = data["account_name"]
        post.post_shares = data["retweets"]

        post.total_views = 0 if data["total_views"] == None else data["total_views"]
        post.prof_img_url = data["profile_image_url"]

        nodes = data["urls"]

        data_engagement = data["likes"] + data["comments"] + data["retweets"]
        total_engagement = data_engagement

        # Media Post
        if data["total_views"] == None and len(nodes) > 0:
            post.post_type = 'a'
            total_engagement = math.ceil(data_engagement/0.76)

        # Video Post
        elif (not data["total_views"] == None) and len(nodes) > 0:
            post.post_type = 'v'
            # total_engagement = data_engagement + data["total_views"]

        # Text Tweet
        else:
            post.post_type = 'p'

        post.post_engagement = total_engagement
        post.post_reach = math.ceil(total_engagement/0.042)

    else:
        post.alive = False

    post.pre_fetched = True
    post.save()
    return data


# def insta_post_update(post_pk):
#     par_post = InstagramPost.objects.get(pk=post_pk)
#     data = get_ig_media_data(par_post.social_id)

#     print("IG Media data fetched!")

#     if "error" not in data:
#         f_post = data
#         print("FOUND!!")
#         print(f_post)
#         par_post.alive = True
#         par_post.likes = f_post["like_count"]
#         par_post.comments = f_post["comments_count"]
#         if "caption" in f_post:
#             par_post.caption = f_post["caption"]
#         par_post.social_id = f_post["id"]

#         dt = dateutil.parser.parse(f_post["timestamp"])
#         par_post.upload_date = dt.astimezone(
#             pytz.timezone("Asia/Kolkata"))

#         data_engagement = f_post["like_count"] + f_post["comments_count"]

#         par_post.post_engagement = data_engagement

#         if f_post["media_type"] == "CAROUSEL_ALBUM":
#             par_post.post_type = "a"
#             par_post.post_reach = math.ceil(data_engagement/0.12)

#         else:
#             if f_post["media_type"] == "VIDEO":
#                 par_post.post_type = "v"
#                 par_post.total_views = math.ceil(data_engagement*10.4)

#             else:
#                 par_post.post_type = "p"
#                 par_post.post_reach = math.ceil(data_engagement/0.12)

#     else:
#         print("failed")
#         par_post.alive = False

#     par_post.pre_fetched = True
#     par_post.save()

#     return data
