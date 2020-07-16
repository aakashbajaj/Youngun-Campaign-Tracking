import re
import requests

from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from django.utils.text import slugify

from .models import Campaign
from youngun.apps.content.models import InstagramStory, FacebookStory, TwitterStory


@receiver(pre_save, sender=Campaign)
def slugify_campaign_if_not_exists(sender, instance, *args, **kwargs):
    if instance and instance.slug == "":
        slug = slugify(instance.name)
        instance.slug = slug


@receiver(pre_save, sender=Campaign)
def update_live_post_story_cnt(sender, instance, *args, **kwargs):
    if instance:
        instance.live_fb_posts = instance.get_facebook_posts.count()
        instance.live_in_posts = instance.get_instagram_posts.count()
        instance.live_tw_posts = instance.get_twitter_posts.count()

        instance.live_fb_stories = instance.get_facebook_stories.count()
        instance.live_in_stories = instance.get_instagram_stories.count()
        instance.live_tw_stories = instance.get_twitter_stories.count()


@receiver(post_save, sender=Campaign)
def fetch_story_screenshots(sender, instance, *args, **kwargs):
    if instance:
        if not instance.in_stories_fetch_ctrl:
            reg_str = r'\["(https:\/\/lh3\.googleusercontent\.com\/[a-zA-Z0-9\-_]*)"'

            resp = requests.get(instance.in_stories_google_photos_album_url)
            resp_str = resp.text

            matches = re.findall(reg_str, resp_str)

            instance.get_instagram_stories.delete()

            for photo_url in matches:
                obj, new_create = InstagramStory.objects.get_or_create(
                    campaign=instance, url=photo_url)

                # obj.save()

            instance.in_stories_fetch_ctrl = True
            instance.save()

        if not instance.fb_stories_fetch_ctrl:
            reg_str = r'\["(https:\/\/lh3\.googleusercontent\.com\/[a-zA-Z0-9\-_]*)"'

            resp = requests.get(instance.fb_stories_google_photos_album_url)
            resp_str = resp.text

            matches = re.findall(reg_str, resp_str)

            instance.get_facebook_stories.delete()

            for photo_url in matches:
                obj, new_create = FacebookStory.objects.get_or_create(
                    campaign=instance, url=photo_url)

                # obj.save()

            instance.fb_stories_fetch_ctrl = True
            instance.save()

        if not instance.tw_stories_fetch_ctrl:
            reg_str = r'\["(https:\/\/lh3\.googleusercontent\.com\/[a-zA-Z0-9\-_]*)"'

            resp = requests.get(instance.tw_stories_google_photos_album_url)
            resp_str = resp.text

            matches = re.findall(reg_str, resp_str)

            instance.get_twitter_stories.delete()

            for photo_url in matches:
                obj, new_create = TwitterStory.objects.get_or_create(
                    campaign=instance, url=photo_url)

                # obj.save()

            instance.tw_stories_fetch_ctrl = True
            instance.save()
