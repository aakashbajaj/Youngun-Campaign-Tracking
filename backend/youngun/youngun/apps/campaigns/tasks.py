import requests
import re

from youngun.apps.campaigns.models import Campaign
from youngun.apps.content.models import InstagramStory, FacebookStory, TwitterStory


def update_live_cnts():
    for camp in Campaign.objects.all():
        if camp:
            camp.live_fb_posts = camp.get_facebook_posts.count()
            camp.live_in_posts = camp.get_instagram_posts.count()
            camp.live_tw_posts = camp.get_twitter_posts.count()

            camp.live_fb_stories = camp.get_facebook_stories.count()
            camp.live_in_stories = camp.get_instagram_stories.count()
            camp.live_tw_stories = camp.get_twitter_stories.count()

            camp.save()


def fetch_campaign_stories():
    for camp in Campaign.objects.all():
        if camp:
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
