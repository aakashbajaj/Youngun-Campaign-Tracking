import requests
from youngun.apps.content.models import Post, InstagramPost, TwitterPost, FacebookPost, PostVisibility

from django_q.tasks import async_task, schedule


def extract_username_from_posts():
    for post in InstagramPost.objects.all():
        post_url = post.url
        fetch_url = "https://api.instagram.com/oembed"
        params = {
            'url': post_url
        }

        res = requests.get(fetch_url, params=params)
        if res.status_code == 404:
            post.visibility = PostVisibility.PRIVATE

        elif res.status_code == 200:
            # fetched_embed = res.json()["html"]
            # post.embed_code = fetched_embed
            post.post_username = res.json()["author_name"]

        post.save()


def extract_all_posts_details():
    for post in Post.objects.all():
        post_url = post.url

        # Instagram post
        if post.platform == "in":
            fill_in_post(post.pk)

        # Twitter Post
        if post.platform == "tw":
            fill_tw_post(post.pk)

        # Facebook Post
        if post.platform == "fb":
            fill_fb_post(post.pk)


def fill_in_post(post_pk):
    async_task("youngun.apps.content.utils.post_filler.in_post_filler", post_pk)


def fill_tw_post(post_pk):
    async_task("youngun.apps.content.utils.post_filler.tw_post_filler", post_pk)


def fill_fb_post(post_pk):
    async_task("youngun.apps.content.utils.post_filler.fb_post_filler", post_pk)
