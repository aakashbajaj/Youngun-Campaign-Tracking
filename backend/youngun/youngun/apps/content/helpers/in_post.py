import requests
import json
from pprint import pprint
from datetime import datetime
import re
import dateutil.parser


class InstagramPostScraper:

    def __init__(self, post_link, resp, __typename):
        self.resp = resp
        self.typename = __typename
        self.data = {"link": post_link,
                     "username": self.resp["owner"]["username"]}

    def get_timestamp(self):
        # return datetime.strftime(datetime.fromtimestamp(self.resp["taken_at_timestamp"]), "%Y-%m-%d %H:%M:%S")
        return datetime.fromtimestamp(self.resp["taken_at_timestamp"])

    def get_comments(self):
        return self.resp["edge_media_to_parent_comment"]["count"]

    def get_caption(self):
        return self.resp["edge_media_to_caption"]["edges"][0]["node"]["text"]

    def get_likes(self):
        return self.resp["edge_media_preview_like"]["count"]

    def get_view_count(self):
        return self.resp["video_view_count"]

    def get_media_url(self, is_video=0):

        if is_video:
            return self.resp["video_url"]
        else:
            return self.resp["display_url"]

    def get_video_data(self):

        X = {
            "timestamp": self.get_timestamp(),
            "likes": self.get_likes(),
            "comments": self.get_comments(),
            "total_views": self.get_view_count(),
            "nodes": [{
                "view_count": self.get_view_count(),
                "media_url": self.get_media_url(1),
                "is_video": True
            }]
        }

        self.data = {**self.data, **X}

    def get_image_data(self):

        X = {
            "timestamp": self.get_timestamp(),
            "likes": self.get_likes(),
            "comments": self.get_comments(),
            "nodes": [{
                "media_url": self.get_media_url(),
                "is_video": False
            }]
        }
    
        self.data = {**self.data, **X}

    def get_sidecar_data(self):

        X = {"likes": self.get_likes(),
             "comments": self.get_comments(),
             "timestamp": self.get_timestamp()}

        self.resp = self.resp["edge_sidecar_to_children"]["edges"]
        result = []
        total_views = 0
        for nodes in self.resp:
            node = nodes["node"]
            if node["is_video"]:
                total_views += node["video_view_count"]
                result.append({"is_video": True,
                               "media_url": node["video_url"],
                               "view_count": node["video_view_count"],
                               "media_key": node["id"]
                               })
            else:
                result.append({"is_video": False,
                               "media_url": node["display_url"],
                               "media_key": node["id"]
                               })

        X["nodes"] = result
        X["total_views"] = total_views
        self.data = {**self.data, **X}

    def get_data(self):

        if self.typename == "GraphImage":
            self.get_image_data()

        elif self.typename == "GraphVideo":
            self.get_video_data()

        else:
            self.get_sidecar_data()

        return self.data


def get_in_post_details(post_link):
    try:
        post_link = post_link.strip('/').strip('?').strip('_')
        resp = requests.get(f"{post_link}/?__a=1").json()
        resp = resp["graphql"]["shortcode_media"]
        __typename = resp["__typename"]
        I = InstagramPostScraper(post_link, resp, __typename)
        data = I.get_data()
        return {"error": None, "result": data}
    except Exception as e:
        print(e)
        return {"error": "An error occurred!!", "result": None, "link": post_link, "msg": str(e)}
