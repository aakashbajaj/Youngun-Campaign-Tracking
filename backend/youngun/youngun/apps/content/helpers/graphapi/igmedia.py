import requests

from django.conf import settings


def get_ig_media_data(media_id):
    access_token = settings.INSTA_GRAPH_LL_TOKEN

    fields = "like_count,caption,comments_count,timestamp,permalink,media_url,media_type,children{media_url,media_type,video_views}"

    params = {
        "fields": fields,
    }
    headers = {
        "Authorization": f"Bearer {access_token}"
    }

    host_url = f"https://graph.facebook.com/v8.0/{media_id}"

    data = requests.get(host_url, params=params, headers=headers)
    resp = data.json()

    try:
        body = resp
        return body
    except Exception as e:
        return {"error": str(e)}
