import dateutil
import pytz
import math

from youngun.apps.content.helpers.graphapi.business_discv import get_business_discovery_user
from youngun.apps.content.helpers.graphapi.igmedia import get_ig_media_data
from youngun.apps.content.helpers.graphapi.iginsights import get_ig_media_insights_data
from youngun.apps.content.models import InstagramPost, FacebookPost, TwitterPost, Post, Media, PostVisibility


def insta_post_filler(post_pk):
    par_post = InstagramPost.objects.get(pk=post_pk)

    if par_post.visibility == PostVisibility.PRIVATE:
        return 

    data = get_business_discovery_user(par_post.post_username)

    print("Business Discovery data fetched!")

    found_post = False
    cnt = 0

    while not found_post:
        print("Running " + str(cnt))
        if "error" not in data:
            print("start search")
            fetched_post_list = data["media"]["data"]

            print("No. of posts:")
            print(len(fetched_post_list))

            for f_post in fetched_post_list:
                if f_post["permalink"] == par_post.url:
                    found_post = True
                    print("FOUND!!")
                    print(f_post)
                    par_post.alive = True
                    par_post.likes = f_post["like_count"]
                    par_post.comments = f_post["comments_count"]
                    if "caption" in f_post:
                        par_post.caption = f_post["caption"]
                    par_post.social_id = f_post["id"]

                    # dt = dateutil.parser.parse(f_post["timestamp"])
                    # par_post.upload_date = dt.astimezone(
                    #     pytz.timezone("Asia/Kolkata"))

                    data_engagement = f_post["like_count"] + \
                        f_post["comments_count"]

                    par_post.post_engagement = data_engagement

                    if f_post["media_type"] == "CAROUSEL_ALBUM":
                        par_post.post_type = "a"
                        par_post.post_reach = math.ceil(data_engagement/0.12)

                    else:
                        if f_post["media_type"] == "VIDEO":
                            par_post.post_type = "v"
                            par_post.total_views = math.ceil(data_engagement*10.4)

                        else:
                            par_post.post_type = "p"
                            par_post.post_reach = math.ceil(data_engagement/0.12)


            if not found_post:
                print("Next Search")
                cnt += 1

                if cnt >= 3:
                    break

                # start next tag search
                if "paging" in data["media"].keys():
                    if "after" in data["media"]["paging"]["cursors"].keys():
                        next_token = data["media"]["paging"]["cursors"]["after"]
                        data = get_business_discovery_user(
                            par_post.post_username, next_token)
                    else:
                        break
                else:
                    break

        else:
            par_post.visibility = PostVisibility.PRIVATE
            break

    if not found_post:
        print("failed")
        par_post.alive = False
        par_post.visibility = PostVisibility.PRIVATE
        # sendlogs(data)

    par_post.pre_fetched = True
    par_post.save()

    return data


def insta_eng_reach_fill(post_pk):
    par_post = InstagramPost.objects.get(pk=post_pk)

    data_engagement = par_post.likes + par_post.comments

    par_post.post_engagement = data_engagement

    if par_post.post_type == "a":
        par_post.post_reach = math.ceil(data_engagement/0.12)

    elif par_post.post_type == "v":
        par_post.total_views = math.ceil(data_engagement*10.4)

    elif par_post.post_type == "p":
        par_post.post_reach = math.ceil(data_engagement/0.12)

    par_post.save()


# def insta_post_fill(post_pk):
#     par_post = InstagramPost.objects.get(pk=post_pk)
#     data = get_business_discovery_user(par_post.post_username)

#     print("Business Discovery data fetched!")

#     if "error" not in data:
#         print("start search")
#         fetched_post_list = data["media"]["data"]

#         print("No. of posts:")
#         print(len(fetched_post_list))

#         for f_post in fetched_post_list:
#             if f_post["permalink"] == par_post.url:
#                 print("FOUND!!")
#                 print(f_post)
#                 par_post.alive = True
#                 par_post.likes = f_post["like_count"]
#                 par_post.comments = f_post["comments_count"]
#                 if "caption" in f_post:
#                     par_post.caption = f_post["caption"]
#                 par_post.social_id = f_post["id"]

#                 dt = dateutil.parser.parse(f_post["timestamp"])
#                 par_post.upload_date = dt.astimezone(
#                     pytz.timezone("Asia/Kolkata"))

#                 par_post.medias.all().delete()

#                 if f_post["media_type"] == "CAROUSEL_ALBUM":
#                     par_post.post_type = "a"
#                     nodes = f_post["children"]["data"]
#                     for node in nodes:
#                         if node["media_type"] == "VIDEO":
#                             media_obj = Media.objects.create(
#                                 parent_post=par_post, url=node["media_url"], key=node["id"], media_type="video")
#                         else:
#                             media_obj = Media.objects.create(
#                                 parent_post=par_post, url=node["media_url"], key=node["id"], media_type="post")

#                 else:
#                     if f_post["media_type"] == "VIDEO":
#                         par_post.post_type = "v"
#                         if "media_url" in f_post:
#                             media_obj = Media.objects.create(
#                                 parent_post=par_post, url=f_post["media_url"], key=f_post["id"], media_type="video")
#                         else:
#                             media_obj = Media.objects.create(
#                                 parent_post=par_post, url="", key=f_post["id"], media_type="video")
#                     else:
#                         par_post.post_type = "p"
#                         media_obj = Media.objects.create(
#                             parent_post=par_post, url=f_post["media_url"], key=f_post["id"], media_type="post")

#             else:
#                 pass

#     else:
#         print("failed")
#         par_post.alive = False
#         # sendlogs(data)

#     par_post.pre_fetched = True
#     par_post.save()

#     return data


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

#         par_post.medias.all().delete()

#         if f_post["media_type"] == "CAROUSEL_ALBUM":
#             par_post.post_type = "a"

#         else:
#             if f_post["media_type"] == "VIDEO":
#                 par_post.post_type = "v"

#             else:
#                 par_post.post_type = "p"

#     else:
#         print("failed")
#         par_post.alive = False
#         # sendlogs(data)

#     # par_post.pre_fetched = True
#     par_post.save()

#     return data


def insta_post_insight_update(post_pk):
    par_post = InstagramPost.objects.get(pk=post_pk)
    data = get_ig_media_insights_data(par_post.social_id, par_post.post_type)

    print("IG Insights data fetched!")

    if "error" not in data:
        f_post = data
        print("FOUND!!")
        print(f_post)

        par_post.post_engagement = f_post["engagement"]
        par_post.post_reach = f_post["reach"]
        par_post.post_saves = f_post["saved"]

        if par_post.post_type == "v":
            par_post.total_views = f_post["video_views"]

        par_post.save()
    else:
        print("failed")
        # par_post.alive = False
        # sendlogs(data)

    # par_post.pre_fetched = True
    par_post.save()

    return data
