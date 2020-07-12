import requests
import re

from youngun.apps.campaigns.models import Campaign
from youngun.apps.content.models import InstagramStory, FacebookStory, TwitterStory


def fetch_stories_google_album():
    for camp in Campaign.objects.all():
        if camp:
            reg_str = r'\["(https:\/\/lh3\.googleusercontent\.com\/[a-zA-Z0-9\-_]*)"'

            # Instagram Stories
            camp.get_instagram_stories.delete()

            resp = requests.get(camp.in_stories_google_photos_album_url)
            resp_str = resp.text
            matches = re.findall(reg_str, resp_str)

            for photo_url in matches:
                obj, _ = InstagramStory.objects.get_or_create(
                    campaign=camp, url=photo_url)

            # FB Stories
            camp.get_facebook_stories.delete()

            resp = requests.get(camp.fb_stories_google_photos_album_url)
            resp_str = resp.text
            matches = re.findall(reg_str, resp_str)

            for photo_url in matches:
                obj, _ = FacebookStory.objects.get_or_create(
                    campaign=camp, url=photo_url)

            # Twitter Stories
            camp.get_twitter_stories.delete()

            resp = requests.get(camp.tw_stories_google_photos_album_url)
            resp_str = resp.text
            matches = re.findall(reg_str, resp_str)

            for photo_url in matches:
                obj, _ = TwitterStory.objects.get_or_create(
                    campaign=camp, url=photo_url)
