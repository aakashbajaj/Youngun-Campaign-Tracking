import requests
from youngun.apps.content.models import Post, InstagramPost, TwitterPost, FacebookPost, PostVisibility
from youngun.apps.content.utils.post_filler import in_post_filler, tw_post_filler, fb_post_filler
from youngun.apps.content.utils.insta_filler import insta_post_update, insta_post_insight_update
from youngun.apps.campaigns.models import Campaign

from django_q.tasks import async_task, schedule
from django.conf import settings


def update_all_active_camp_metrics():
    opts = {'group': 'update_all_active_camp_metrics'}
    for camp in Campaign.objects.all():
        if camp.status == "active":
            async_task(
                "youngun.apps.content.tasks.update_camp_post_metrics", camp.pk, camp.name, q_options=opts)


def update_all_camp_metrics():
    opts = {'group': 'update_all_camp_metrics'}
    for camp in Campaign.objects.all():
        async_task(
            "youngun.apps.content.tasks.update_camp_post_metrics", camp.pk, camp.name, q_options=opts)

# Utility Tasks


def extract_username_from_posts():
    for post in InstagramPost.objects.all():
        post_url = post.url
        fetch_url = "https://graph.facebook.com/v8.0/instagram_oembed"
        params = {
            'url': post_url
        }

        headers = {
            'Authorization': "Bearer " + settings.INSTA_AUTH_TOKEN
        }

        res = requests.get(fetch_url, params=params, headers=headers)

        if res.status_code == 404:
            post.visibility = PostVisibility.PRIVATE

        elif res.status_code == 200:
            post.post_username = res.json()["author_name"]

        post.save()


def update_camp_post_metrics(camp_pk, camp_name):
    print(f"Processing {camp_name}")
    camp = Campaign.objects.get(pk=camp_pk)
    for post in camp.posts.all():
        # Instagram post
        if post.platform == "in":
            insta_post_update(post.pk)
            # insta_post_insight_update(post.pk)

        # Twitter Post
        if post.platform == "tw":
            tw_post_filler(post.pk)

        # Facebook Post
        if post.platform == "fb":
            fb_post_filler(post.pk)

    return f"Success: {camp.name}"


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
    opts = {'group': "single-post-metric-fetch"}
    async_task("youngun.apps.content.utils.post_filler.in_post_filler",
               post_pk, q_options=opts)


def fill_tw_post(post_pk):
    opts = {'group': "single-post-metric-fetch"}
    async_task("youngun.apps.content.utils.post_filler.tw_post_filler",
               post_pk, q_options=opts)


def fill_fb_post(post_pk):
    opts = {'group': "single-post-metric-fetch"}
    async_task("youngun.apps.content.utils.post_filler.fb_post_filler",
               post_pk, q_options=opts)


def fill_in_post_graphapi(post_pk):
    opts = {'group': "graphapi-single-post-metric-fetch"}
    async_task("youngun.apps.content.utils.insta_filler.insta_post_fill",
               post_pk, q_options=opts)


def update_in_post_graphapi(post_pk):
    opts = {'group': "graphapi-single-post-metric-update"}
    async_task("youngun.apps.content.utils.insta_filler.insta_post_update",
               post_pk, q_options=opts)


def update_insights_in_post_graphapi(post_pk):
    opts = {'group': "graphapi-single-post-metric-update"}
    async_task("youngun.apps.content.utils.insta_filler.insta_post_insight_update",
               post_pk, q_options=opts)
