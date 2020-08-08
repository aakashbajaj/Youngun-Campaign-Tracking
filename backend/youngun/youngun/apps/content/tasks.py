import requests
from youngun.apps.content.models import InstagramPost, TwitterPost, FacebookPost, PostVisibility


def extract_username_from_posts():
    for post in InstagramPost.objects.all():
        post_url = post.url
        fetch_url = "https://api.instagram.com/oembed"
        params = {
            'url': post_url
        }

        res = requests.get(fetch_url, params=params)
        if res.status_code == 404:
            post.visibility = PostVisibility.PRIVATE

        elif res.status_code == 200:
            # fetched_embed = res.json()["html"]
            # post.embed_code = fetched_embed
            post.post_username = res.json()["author_name"]

        post.save()
