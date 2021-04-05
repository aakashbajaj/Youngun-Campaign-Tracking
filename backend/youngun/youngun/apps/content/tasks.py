from youngun.apps.content.models import Post, InstagramPost, TwitterPost, FacebookPost, PostVisibility
from youngun.apps.content.utils.post_filler import in_post_filler, tw_post_filler, fb_post_filler, tw_eng_reach_fill
from youngun.apps.content.utils.post_update import tw_post_updater
from youngun.apps.content.utils.insta_filler import insta_post_filler, insta_eng_reach_fill
from youngun.apps.campaigns.models import Campaign
from youngun.apps.campaigns.tasks import update_all_active_camp_engagement_data

from django_q.tasks import async_task, schedule
from django.conf import settings
from django.db.models import Count, Sum

import requests
import time
import json
import datetime
from pprint import pprint


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



def update_latest_tweets_metrics():
    today_min = datetime.datetime.combine(
        datetime.date.today(), datetime.time.min)
    days_3_ago = today_min - datetime.timedelta(days=3)
    results = TwitterPost.objects.filter(
        campaign__status="active").filter(upload_date__gte=days_3_ago)
    pk_list = [x for x in results.values_list('pk', flat=True)]

    opts = {'group': 'update_latest_tweets_metrics'}
    async_task("youngun.apps.content.tasks.update_tw_post_metric",
               pk_list, q_options=opts)


def update_all_tweets_metrics():
    results = TwitterPost.objects.filter(campaign__status="active")
    pk_list = [x for x in results.values_list('pk', flat=True)]

    print("Trigger All Twitter Update")

    opts = {'group': 'update_all_tweets_metrics'}
    async_task("youngun.apps.content.tasks.update_tw_post_metric",
               pk_list, q_options=opts)

# Tweets data - images etc update

def update_all_tweets_data():
    results = TwitterPost.objects.filter(campaign__status="active")
    pk_list = [x for x in results.values_list('pk', flat=True)]

    print("Trigger All Twitter Data Refresh")

    opts = {'group': 'update_all_tweets_data'}
    async_task("youngun.apps.content.tasks.update_tw_post_data",
               pk_list, q_options=opts)

# Engagement/Reach Update Calls

def update_all_tweets_eng_reach():
    results = TwitterPost.objects.filter(campaign__status="active")
    pk_list = [x for x in results.values_list('pk', flat=True)]

    print("Trigger All Twitter Eng/Reach Update")

    opts = {'group': 'update_all_tweets_eng_reach'}
    async_task("youngun.apps.content.tasks.update_tw_post_eng_reach",
               pk_list, q_options=opts)

def update_all_insta_eng_reach():
    results = InstagramPost.objects.filter(campaign__status="active")
    pk_list = [x for x in results.values_list('pk', flat=True)]

    print("Trigger All Instagram Eng/Reach Update")

    opts = {'group': 'update_all_insta_eng_reach'}
    async_task("youngun.apps.content.tasks.update_in_post_eng_reach",
               pk_list, q_options=opts)


def update_latest_insta_metrics():
    today_min = datetime.datetime.combine(
        datetime.date.today(), datetime.time.min)
    days_3_ago = today_min - datetime.timedelta(days=3)
    results = InstagramPost.objects.filter(
        campaign__status="active").filter(visibility=PostVisibility.PUBLIC).filter(upload_date__gte=days_3_ago)
    pk_list = [x for x in results.values_list('pk', flat=True)]

    print("Trigger Latest Insta Update")

    opts = {'group': 'update_latest_insta_metrics'}
    async_task("youngun.apps.content.tasks.update_in_post_metric",
               pk_list, q_options=opts)


def update_all_insta_metrics():
    results = InstagramPost.objects.filter(campaign__status="active").filter(visibility=PostVisibility.PUBLIC)
    pk_list = [x for x in results.values_list('pk', flat=True)]

    print("Trigger All Insta Update")

    opts = {'group': 'update_all_insta_metrics'}
    async_task("youngun.apps.content.tasks.update_in_post_metric",
               pk_list, q_options=opts)

# Worker Tasks

def update_tw_post_metric(post_pk_list):
    for post_pk in post_pk_list:
        tw_post_updater(post_pk)
        time.sleep(4)

    # call fn to update campaign engagement metric
    # update_all_active_camp_engagement_data()

def update_tw_post_data(post_pk_list):
    for post_pk in post_pk_list:
        tw_post_filler(post_pk)
        time.sleep(4)


def update_in_post_metric(post_pk_list):
    for post_pk in post_pk_list:
        print("In loop!!")
        insta_post_filler(post_pk)
        print(post_pk_list)
        print(post_pk)
        print("Done 1")
        time.sleep(60)

    print("Update Complete!!")

    # call fn to update campaign engagement metric
    # update_all_active_camp_engagement_data()

def update_in_post_eng_reach(post_pk_list):
    print("Start All Instagram Eng/Reach Update")
    for post_pk in post_pk_list:
        insta_eng_reach_fill(post_pk)

    print("Complete All Instagram Eng/Reach Update")

def update_tw_post_eng_reach(post_pk_list):
    print("Start All Twitter Eng/Reach Update")
    for post_pk in post_pk_list:
        tw_eng_reach_fill(post_pk)

    print("Complete All Twitter Eng/Reach Update")




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
    # for post in camp.posts.all():
    #     # Instagram post
    #     if post.platform == "in":
    #         insta_post_filler(post.pk)
    #         # insta_post_insight_update(post.pk)

    #     # Twitter Post
    #     if post.platform == "tw":
    #         tw_post_filler(post.pk)

    #     # Facebook Post
    #     if post.platform == "fb":
    #         fb_post_filler(post.pk)

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
    async_task("youngun.apps.content.utils.insta_filler.insta_post_filler",
               post_pk, q_options=opts)


def update_in_post_graphapi(post_pk):
    opts = {'group': "graphapi-single-post-metric-update"}
    async_task("youngun.apps.content.utils.insta_filler.insta_post_filler",
               post_pk, q_options=opts)


def update_insights_in_post_graphapi(post_pk):
    opts = {'group': "graphapi-single-post-metric-update"}
    async_task("youngun.apps.content.utils.insta_filler.insta_post_insight_update",
               post_pk, q_options=opts)

# def update_in_post_eng_reach(post_pk):
#     opts = {'group': "in-post-eng-reach-update"}
#     async_task("youngun.apps.content.utils.insta_filler.insta_eng_reach_fill",
#                post_pk, q_options=opts)

# def update_tw_post_eng_reach(post_pk):
#     opts = {'group': "tw-post-eng-reach-update"}
#     async_task("youngun.apps.content.utils.post_filler.tw_eng_reach_fill",
#                post_pk, q_options=opts)