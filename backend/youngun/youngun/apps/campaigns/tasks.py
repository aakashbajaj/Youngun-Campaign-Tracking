import requests
import re

from django_q.tasks import async_task, schedule
from django.db.models import Count, Sum

from youngun.apps.campaigns.models import Campaign
from youngun.apps.content.models import Post
from youngun.apps.content.models import InstagramStory, FacebookStory, TwitterStory


def update_v2_active_camp_metrics():
    opts = {'group': 'update_v2_active_camp_metrics'}
    for camp in Campaign.objects.all():
        if camp.status == "active" and camp.campaign_module == "v2":
            async_task("youngun.apps.content.tasks.update_camp_post_metrics",
                       camp.pk, camp.name, q_options=opts)


def trigger_update_campaign_report_metrics():
    opts = {'group': 'update_campaign_report_metrics'}
    for camp in Campaign.objects.all():
        if camp.status == "active" and camp.campaign_module == "v2":
            async_task("youngun.apps.campaigns.tasks.update_campaign_report_metrics",
                       camp.pk, camp.name, q_options=opts)


def update_all_active_camp_engagement_data():
    # opts = {'group': 'update_all_active_camp_metrics'}
    for camp in Campaign.objects.all():
        if camp.status == "active":
            camp_reach = camp.posts.all().aggregate(Sum('post_reach'))[
                'post_reach__sum'] + camp.posts.all().aggregate(Sum('total_views'))['total_views__sum']
            camp_engagement = camp.posts.all().aggregate(
                Sum('post_engagement'))['post_engagement__sum']


            if camp.posts.filter(platform="in").count() > 0:
                in_reach = camp.posts.filter(platform="in").aggregate(Sum('post_reach'))[
                    'post_reach__sum'] + camp.posts.filter(platform="in").aggregate(Sum('total_views'))['total_views__sum']
                
                in_engagement = camp.posts.filter(platform="in").aggregate(
                    Sum('post_engagement'))['post_engagement__sum']
                
                camp.in_engagement = in_engagement
                camp.in_reach = in_reach

            if camp.posts.filter(platform="tw").count() > 0:
                tw_reach = camp.posts.filter(platform="tw").aggregate(Sum('post_reach'))[
                    'post_reach__sum'] + camp.posts.filter(platform="tw").aggregate(Sum('total_views'))['total_views__sum']
                
                tw_engagement = camp.posts.filter(platform="tw").aggregate(
                    Sum('post_engagement'))['post_engagement__sum']

                camp.tw_engagement = tw_engagement
                camp.tw_reach = tw_reach

            
            if camp.posts.filter(platform="fb").count() > 0:
                fb_reach = camp.posts.filter(platform="fb").aggregate(Sum('post_reach'))[
                    'post_reach__sum'] + camp.posts.filter(platform="fb").aggregate(Sum('total_views'))['total_views__sum']

            
                fb_engagement = camp.posts.filter(platform="fb").aggregate(
                    Sum('post_engagement'))['post_engagement__sum']

                camp.fb_engagement = fb_engagement
                camp.fb_reach = fb_reach

            
            camp.total_post_engagement = camp_engagement
            camp.total_campaign_reach = camp_reach
            
            camp.num_posts = camp.posts.all().count()

            camp.save()


def update_campaign_report_metrics(camp_pk, camp_name):
    print(f"Processing {camp_name}")
    camp = Campaign.objects.get(pk=camp_pk)

    camp.num_posts = camp.posts.all().count()

    engagement = 0
    shares = 0
    saves = 0
    video_views = 0
    reach = 0

    for post in camp.posts.all():
        engagement = engagement + post.post_engagement
        shares = shares + post.post_shares
        saves = saves + post.post_saves
        video_views = video_views + post.total_views
        reach = reach + post.post_reach

    camp.post_engagement = engagement
    camp.post_shares = shares
    camp.post_saves = saves
    camp.video_views = video_views
    camp.post_reach = reach

    camp.save()

    return f"Success: {camp.name}"


def bulk_upload_csv(posts_list, campaign_id):
    opts = {'group': "csv-bulk-post-upload"}
    async_task('youngun.apps.campaigns.tasks.upload_posts_lists',
               posts_list, campaign_id, q_options=opts)


def upload_posts_lists(posts_list, campaign_id):
    cnt = 0
    for post in posts_list:
        
        try:
            p_obj, created = Post.objects.get_or_create(
                campaign=Campaign.objects.get(id=campaign_id), url=post)
            if created:
                cnt = cnt + 1

            if "facebook.com" in post:
                p_obj.platform = "fb"
                if "/video" in post:
                    p_obj.post_type = "video"
                else:
                    p_obj.post_type = "post"
            elif "instagram.com" in post:
                p_obj.platform = "in"
                p_obj.embed_code = ""
            elif "twitter.com" in post:
                p_obj.platform = "tw"
                p_obj.embed_code = ""

            p_obj.save()
        
        except:
            print("Failed to add " + post + " in " + campaign_id)


# def update_live_cnts():
#     for camp in Campaign.objects.all():
#         if camp:
#             camp.live_fb_posts = camp.get_facebook_posts.count()
#             camp.live_in_posts = camp.get_instagram_posts.count()
#             camp.live_tw_posts = camp.get_twitter_posts.count()

#             camp.live_fb_stories = camp.get_facebook_stories.count()
#             camp.live_in_stories = camp.get_instagram_stories.count()
#             camp.live_tw_stories = camp.get_twitter_stories.count()

#             camp.save()


def fetch_campaign_stories():
    for camp in Campaign.objects.all():
        if camp:
            try:
                reg_str = r'\["(https:\/\/lh3\.googleusercontent\.com\/[a-zA-Z0-9\-_]*)"'

                resp = requests.get(camp.in_stories_google_photos_album_url)
                resp_str = resp.text

                matches = re.findall(reg_str, resp_str)

                camp.get_instagram_stories.delete()

                for photo_url in matches:
                    obj, new_create = InstagramStory.objects.get_or_create(
                        campaign=camp, url=photo_url)

                resp = requests.get(camp.fb_stories_google_photos_album_url)
                resp_str = resp.text

                matches = re.findall(reg_str, resp_str)

                camp.get_facebook_stories.delete()

                for photo_url in matches:
                    obj, new_create = FacebookStory.objects.get_or_create(
                        campaign=camp, url=photo_url)

                resp = requests.get(camp.tw_stories_google_photos_album_url)
                resp_str = resp.text

                matches = re.findall(reg_str, resp_str)

                camp.get_twitter_stories.delete()

                for photo_url in matches:
                    obj, new_create = TwitterStory.objects.get_or_create(
                        campaign=camp, url=photo_url)

            except Exception as e:
                print(str(e))
