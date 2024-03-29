from pprint import pprint
from datetime import datetime
import math

from youngun.apps.content.helpers import in_post, fb_post, tw_post
from youngun.apps.content.models import InstagramPost, FacebookPost, TwitterPost, Post, Media

# from youngun.apps.core.utils import sendlogs


def in_post_filler(post_pk):
    post = InstagramPost.objects.get(pk=post_pk)
    data = in_post.get_in_post_details(post.url)

    # sendlogs(data)
    pprint(data)
    print(data["error"])

    if data["error"] is None:
        print("started")
        data = data["result"]

        post.alive = True
        post.likes = data["likes"]
        post.comments = data["comments"]
        post.post_username = data["username"]
        post.caption = data["caption"]
        post.upload_date = datetime.strptime(data["timestamp"], "%Y-%m-%d %H:%M:%S")

        curr_media = post.medias.all()
        nodes = data["nodes"]

        print("current media: ",len(curr_media))

        # media object already exist, just overwrite to ensure the details are updated
        if len(curr_media) == len(nodes):
            print("Editing!!")
            for i, node in enumerate(nodes):
                media_obj = curr_media[i]

                if node["is_video"]:
                    media_obj.url = node["media_url"]
                    media_obj.key = node["media_key"]
                    media_obj.media_type = "video"
                    media_obj.media_views = node["view_count"]
                else:
                    media_obj.url = node["media_url"]
                    media_obj.key = node["media_key"]
                    media_obj.media_type = "post"

                media_obj.save()

        # media objects don't match -> delete previous and fetch new
        else:
            print("Creating!!")
            post.medias.all().delete()
            for node in data["nodes"]:
                if node["is_video"]:
                    media_obj = Media.objects.create(
                        parent_post=post, url=node["media_url"], key=node["media_key"], media_type="video", media_views=node["view_count"])
                else:
                    media_obj = Media.objects.create(
                        parent_post=post, url=node["media_url"], key=node["media_key"], media_type="post")

    else:
        print("failed")
        post.alive = False
        # sendlogs(data)

    post.pre_fetched = True
    post.save()

    return data


def tw_post_filler(post_pk):
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
        # post.upload_date = datetime.strptime(data["timestamp"], "%Y-%m-%d %H:%M:%S")
        post.account_name = data["account_name"]
        post.post_shares = data["retweets"]

        post.total_views = 0 if data["total_views"] == None else data["total_views"]
        post.prof_img_url = data["profile_image_url"]

        curr_media = post.medias.all()
        nodes = data["urls"]
        data_engagement = data["likes"] + data["comments"] + data["retweets"]
        total_engagement = data_engagement

        post.medias.all().delete()

        # if data["view_count"] == None and nodes == []:
        #     post.medias.all().delete()

        # Media Post
        if data["total_views"] == None and len(nodes) > 0:
            post.post_type = 'a'
            total_engagement = math.ceil(data_engagement/0.76)
            for node in nodes:
                # if not node["is_video"]:
                media_obj = Media.objects.create(
                    parent_post=post, url=node["media_url"], key=node["media_key"], media_type="post")
                media_obj.save()

        # Video Post
        elif (not data["total_views"] == None) and len(nodes) > 0:
            post.post_type = 'v'
            # total_engagement = data_engagement + data["total_views"]
            node = nodes[0]
            media_obj = Media.objects.create(
                parent_post=post, url=node["media_url"], key=node["media_key"], media_type="video", media_views=data["total_views"])
            media_obj.save()

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


def fb_post_filler(post_pk):
    post = FacebookPost.objects.get(pk=post_pk)
    # data = fb_post.get_fb_post_details(post.url)


def tw_eng_reach_fill(post_pk):
    post = TwitterPost.objects.get(pk=post_pk)

    data_engagement = post.likes + post.comments + post.post_shares
    total_engagement = data_engagement

    if post.post_type == 'a':
        total_engagement = math.ceil(data_engagement/0.76)

    elif post.post_type == 'v':
        pass

    post.post_engagement = total_engagement
    post.post_reach = math.ceil(total_engagement/0.042)

    post.save()