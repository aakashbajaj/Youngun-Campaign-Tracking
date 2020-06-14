from django.db.models.signals import pre_save
from django.dispatch import receiver

import requests

from .models import Post, PostVisibility, InstagramPost


@receiver(pre_save, sender=InstagramPost)
def fetch_insta_embed_code(sender, instance, *args, **kwargs):
    if instance and instance.platform == "in":
        if not instance.embed_code.startswith("<blockquote"):
            post_url = instance.url
            fetch_url = "https://api.instagram.com/oembed"
            params = {
                'url': post_url
            }

            res = requests.get(fetch_url, params=params)
            if res.status_code == 404:
                instance.visibility = PostVisibility.PRIVATE

            elif res.status_code == 200:
                instance.embed_code = res.json()["html"]
