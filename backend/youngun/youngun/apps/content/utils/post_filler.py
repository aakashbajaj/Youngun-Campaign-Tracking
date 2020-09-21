from youngun.apps.content.helpers import in_post, fb_post, tw_post
from youngun.apps.content.models import InstagramPost, FacebookPost, TwitterPost, Post, Media


def in_post_filler(post_pk):
    post = InstagramPost.objects.get(pk=post_pk)
    data = in_post.get_in_post_details(post.url)

    if data["error"] is not None:
        data = data["result"]

        post.alive = True
        post.likes = data["likes"]
        post.comments = data["comments"]
        post.post_username = data["username"]
        post.caption = data["caption"]
        post.upload_date = data["timestamp"]

        curr_media = post.medias.all()
        nodes = data["nodes"]

        if len(curr_media) == len(nodes):
            for i, node in enumerate(nodes):
                media_obj = curr_media[i]

                if node["is_video"]:
                    media_obj.url = node["media_url"]
                    media_obj.key = node["media_key"]
                    media_obj.media_type = "video"
                    media_obj.media_views = node["view_count"]
                if node["is_video"]:
                    media_obj.url = node["media_url"]
                    media_obj.key = node["media_key"]
                    media_obj.media_type = "post"

                media_obj.save()
        else:
            post.medias.all().delete()
            for node in data["nodes"]:
                if node["is_video"]:
                    media_obj = Media.objects.create(
                        parent_post=post, url=node["media_url"], key=node["media_key"], media_type="video", media_views=node["view_count"])
                if node["is_video"]:
                    media_obj = Media.objects.create(
                        parent_post=post, url=node["media_url"], key=node["media_key"], media_type="post")

    else:
        post.alive = False

    post.save()


def tw_post_filler(post_pk):
    post = TwitterPost.objects.get(pk=post_pk)
    data = tw_post.get_tw_post_details(post.url)

    if data["error"] is not None:
        data = data["result"]

        post.alive = True
        post.likes = data["likes"]
        post.comments = data["comments"]
        post.post_username = data["username"]
        post.caption = data["caption"]
        post.upload_date = data["timestamp"]
        post.account_name = data["account_name"]

        curr_media = post.medias.all()
        nodes = data["urls"]

        post.medias.all().delete()

        # if data["view_count"] == None and nodes == []:
        #     post.medias.all().delete()

        if data["view_count"] == None and len(nodes) > 0:
            for node in nodes:
                if node["is_video"]:
                    media_obj = Media.objects.create(
                        parent_post=post, url=node["media_url"], key=node["media_key"], media_type="post")
                    media_obj.save()

        elif (not data["view_count"] == None) and len(nodes) > 0:
            media_obj = Media.objects.create(
                parent_post=post, url=node["media_url"], key=node["media_key"], media_type="video", media_views=data["view_count"])
            media_obj.save()

    else:
        post.alive = False

    post.save()


def fb_post_filler(post_pk):
    post = FacebookPost.objects.get(pk=post_pk)
    data = fb_post.get_fb_post_details(post.url)
