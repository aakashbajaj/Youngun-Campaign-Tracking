from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver

import requests

from youngun.apps.content.models import Post, PostVisibility, InstagramPost, TwitterPost, FacebookPost
from youngun.apps.content.tasks import fill_in_post, fill_tw_post, fill_fb_post


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
                instance.post_username = res.json()["author_name"]


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


@receiver(post_save, sender=InstagramPost)
def fetch_in_post(sender, instance, *args, **kwargs):
    fill_in_post(instance.pk)


@receiver(post_save, sender=TwitterPost)
def fetch_tw_post(sender, instance, *args, **kwargs):
    fill_tw_post(instance.pk)


@receiver(post_save, sender=FacebookPost)
def fetch_fb_post(sender, instance, *args, **kwargs):
    fill_fb_post(instance.pk)


@receiver(post_save, sender=Post)
def fetch_insta_post(sender, instance, *args, **kwargs):
    if instance.platform == "in":
        fill_in_post(instance.pk)
    if instance.platform == "in":
        fill_tw_post(instance.pk)
    if instance.platform == "in":
        fill_fb_post(instance.pk)
