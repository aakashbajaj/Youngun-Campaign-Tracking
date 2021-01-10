from pprint import pprint
from datetime import datetime
import math

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
        post.upload_date = datetime.strptime(data["timestamp"], "%Y-%m-%d %H:%M:%S")
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