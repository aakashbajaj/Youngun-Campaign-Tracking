import re
import requests

from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from django.utils.text import slugify

from .models import Campaign
from youngun.apps.content.models import Story


@receiver(pre_save, sender=Campaign)
def slugify_campaign_if_not_exists(sender, instance, *args, **kwargs):
    if instance:
        slug = slugify(instance.name)
        instance.slug = slug


@receiver(post_save, sender=Campaign)
def fetch_story_screenshots(sender, instance, *args, **kwargs):
    if instance:
        if not instance.stories_fetch_ctrl:
            reg_str = r'\["(https:\/\/lh3\.googleusercontent\.com\/[a-zA-Z0-9\-_]*)"'

            resp = requests.get(instance.stories_google_photos_album_url)
            resp_str = resp.text

            matches = re.findall(reg_str, resp_str)

            for photo_url in matches:
                obj, new_create = Story.objects.get_or_create(
                    campaign=instance, url=photo_url)

                # obj.save()

            instance.stories_fetch_ctrl = True
            instance.save()
