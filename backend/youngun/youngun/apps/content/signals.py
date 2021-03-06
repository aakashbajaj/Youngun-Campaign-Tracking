from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver

import requests
from datetime import datetime

from youngun.apps.content.models import Post, PostVisibility, InstagramPost, TwitterPost, FacebookPost
from youngun.apps.content.tasks import fill_in_post, fill_tw_post, fill_fb_post, fill_in_post_graphapi

from django.conf import settings


@receiver(pre_save, sender=InstagramPost)
@receiver(pre_save, sender=Post)
def fetch_insta_embed_code(sender, instance, *args, **kwargs):
    if instance and instance.platform == "in":
        if not instance.embed_code.startswith("<blockquote"):
            post_url = instance.url
            fetch_url = "https://graph.facebook.com/v8.0/instagram_oembed"
            params = {
                'url': post_url
            }
            headers = {
                'Authorization': "Bearer " + settings.INSTA_AUTH_TOKEN
            }

            res = requests.get(fetch_url, params=params, headers=headers)

            if res.status_code == 200:
                fetched_embed = res.json()["html"]
                instance.embed_code = fetched_embed
                instance.post_username = res.json()["author_name"]

                if "instagram.com/reel/" in fetched_embed:
                    instance.visibility = PostVisibility.PRIVATE

            else:
                instance.visibility = PostVisibility.PRIVATE

            if "/reel/" in instance.url:
                instance.visibility = PostVisibility.PRIVATE

            if "?" in post_url:
                post_url = post_url.split("?")[0]

            if not post_url[-1] == "/":
                post_url = post_url + "/" 

            instance.url = post_url


@receiver(pre_save, sender=TwitterPost)
@receiver(pre_save, sender=Post)
def fetch_twitter_embed_code(sender, instance, *args, **kwargs):
    if instance and instance.platform == "tw":
        if "?" in instance.url:
            instance.url = instance.url[:(instance.url.index("?"))]
        if not instance.embed_code.startswith("<blockquote"):
            post_url = instance.url
            fetch_url = "https://publish.twitter.com/oembed"
            params = {
                'url': post_url
            }

            res = requests.get(fetch_url, params=params)
            instance.upload_date = datetime.now()
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

        if not instance.pre_fetched:
            instance.upload_date = datetime.now()
            instance.pre_fetched = True


# @receiver(post_save, sender=InstagramPost)
# def fetch_in_post(sender, instance, *args, **kwargs):
#     if instance and instance.platform == "in":
#         if not instance.pre_fetched:
#             fill_in_post(instance.pk)

@receiver(post_save, sender=Post)
@receiver(post_save, sender=InstagramPost)
def set_upload_date_in(sender, instance, created, *args, **kwargs):
    if created:
        instance.upload_date = datetime.now()
        instance.save()

@receiver(post_save, sender=Post)
@receiver(post_save, sender=TwitterPost)
def set_upload_date_tw(sender, instance, created, *args, **kwargs):
    if created:
        instance.upload_date = datetime.now()
        instance.save()

@receiver(post_save, sender=Post)
@receiver(post_save, sender=FacebookPost)
def set_upload_date_fb(sender, instance, created, *args, **kwargs):
    if created:
        instance.upload_date = datetime.now()
        instance.save()
        
            

# @receiver(post_save, sender=TwitterPost)
# def fetch_tw_post(sender, instance, created, *args, **kwargs):
#     if instance and instance.platform == "tw":
#         if not instance.pre_fetched:
#             fill_tw_post(instance.pk)
        
#         if created:
#             instance.upload_date = datetime.now()


# @receiver(post_save, sender=FacebookPost)
# def fetch_fb_post(sender, instance, created, *args, **kwargs):
#     if instance and instance.platform == "fb":
#         # if not instance.pre_fetched:
#         #     fill_fb_post(instance.pk)
#         if created:
#             instance.upload_date = datetime.now()


# @receiver(post_save, sender=Post)
# def fetch_insta_post(sender, instance, *args, **kwargs):
#     if instance:
#         if not instance.pre_fetched:
#             # if instance.platform == "in":
#             #     fill_in_post(instance.pk)
#             if instance.platform == "tw":
#                 fill_tw_post(instance.pk)
#             # if instance.platform == "fb":
#             #     fill_fb_post(instance.pk)
