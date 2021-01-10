import requests
import json
from datetime import datetime, timedelta
import pytz
import re
import dateutil.parser

from django.conf import settings

class TwitterPostScraper:

    def __init__(self, post_link, resp):
        self.resp = resp
        self.data = {"link": post_link}

    def get_username(self):
        return self.resp.get('includes').get('users')[0].get('username')

    def get_profile_img_url(self):
        return self.resp.get('includes').get('users')[0].get('profile_image_url')

    def get_account_name(self):
        return self.resp.get('includes').get('users')[0].get('name')

    def get_timestamp(self):
        dt = dateutil.parser.parse(self.resp.get('data')[0].get('created_at'))
        return datetime.strftime(dt.astimezone(pytz.timezone("Asia/Kolkata")), "%Y-%m-%d %H:%M:%S")

    def get_caption(self):
        return self.resp['data'][0].get('text')

    def get_likes(self):
        return self.resp['data'][0].get('public_metrics').get('like_count')

    def get_retweet(self):
        return self.resp['data'][0].get('public_metrics').get('retweet_count')

    def get_replies(self):
        return self.resp['data'][0].get('public_metrics').get('reply_count')

    def media_exists(self):
        return self.resp.get('includes').get('media')

    def get_media(self):
        url = []
        if self.resp.get('includes').get('media')[0].get('type') == 'video':
            views = self.resp.get('includes').get('media')[0].get(
                'public_metrics').get('view_count')
            media_obj = {
                'media_url': self.resp.get('includes').get('media')[0].get('preview_image_url'),
                'media_key': self.resp.get('includes').get('media')[0].get('media_key'),
                'is_video': True,
                'view_count': views
            }
            url.append(media_obj)
        else:
            views = None
            for i in self.resp.get('includes').get('media'):
                media_obj = {
                    'media_url': i.get('url'),
                    'media_key': i.get('media_key'),
                    'is_video': False
                }
                url.append(media_obj)
        return views, url

    def get_data(self):
        X = {
            'username': self.get_username(),
            'account_name': self.get_account_name(),
            'profile_image_url': self.get_profile_img_url(),
            'timestamp': self.get_timestamp(),
            'likes': self.get_likes(),
            'caption': self.get_caption(),
            'comments': self.get_replies(),
            'retweets': self.get_retweet(),
            'total_views': self.get_media()[0] if self.media_exists() else None,
            'urls': self.get_media()[1] if self.media_exists() else [],
        }
        self.data = {**self.data, **X}
        return self.data


def tw_headers_and_params():

    headers = {
        'Authorization': 'Bearer ' + settings.TWITTER_AUTH_TOKEN,
    }

    params = (
        ('expansions', 'author_id,attachments.media_keys'),
        ('tweet.fields', 'public_metrics,created_at'),
        ('user.fields', 'username,verified,profile_image_url'),
        ('media.fields', 'public_metrics,preview_image_url,url'),
    )
    return headers, params


def get_tw_post_details(post_link):
    num = int(post_link.strip('/').split('/')[-1])
    try:
        resp = requests.get(f'https://api.twitter.com/2/tweets?ids={num}', headers=tw_headers_and_params()[
                            0], params=tw_headers_and_params()[1]).json()
        tw = TwitterPostScraper(post_link, resp)
        data = tw.get_data()

        return {"error": None, "result": data}
    except Exception as e:
        # print(e)
        return {"error": "An error occurred!!", "result": None, "link": post_link, "msg": str(e)}
