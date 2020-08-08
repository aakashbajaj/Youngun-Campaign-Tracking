from django.db.models.signals import pre_save
from django.dispatch import receiver

import requests

from .models import Post, PostVisibility, InstagramPost, TwitterPost, FacebookPost


@receiver(pre_save, sender=InstagramPost)
@receiver(pre_save, sender=Post)
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
                fetched_embed = res.json()["html"]
                instance.embed_code = fetched_embed

            if fetched_embed.startswith("<blockquote"):
                start_idx = fetched_embed.index("(@")
                if start_idx > 0:
                    end_idx = fetched_embed[start_idx:].index(")")
                    instance.post_username = fetched_embed[start_idx +
                                                           2:end_idx+start_idx]


@receiver(pre_save, sender=TwitterPost)
@receiver(pre_save, sender=Post)
def fetch_twitter_embed_code(sender, instance, *args, **kwargs):
    if instance and instance.platform == "tw":
        if not instance.embed_code.startswith("<blockquote"):
            post_url = instance.url
            fetch_url = "https://publish.twitter.com/oembed"
            params = {
                'url': post_url
            }

            res = requests.get(fetch_url, params=params)
            if res.status_code == 404:
                instance.visibility = PostVisibility.PRIVATE

            elif res.status_code == 200:
                instance.embed_code = res.json()["html"]


@receiver(pre_save, sender=FacebookPost)
@receiver(pre_save, sender=Post)
def save_facebook_info(sender, instance, *args, **kwargs):
    if instance and instance.platform == "fb":
        post_url = instance.url

        if "/video" in post_url:
            instance.post_type = "v"
        else:
            instance.post_type = "p"

        instance.embed_code = ""
