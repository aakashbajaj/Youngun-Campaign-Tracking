import requests

from django.conf import settings


def get_ig_media_insights_data(media_id, media_type):
    access_token = settings.INSTA_GRAPH_LL_TOKEN

    metrics = ""
    if media_type == "a":
        metrics = "carousel_album_engagement,carousel_album_impressions,carousel_album_reach,carousel_album_saved,carousel_album_video_views"
    elif media_type == "v":
        metrics = "engagement,video_views,saved,impressions,reach"
    elif media_type == "p":
        metrics = "engagement,saved,impressions,reach"
    params = {
        "metric": metrics,
    }
    headers = {
        "Authorization": f"Bearer {access_token}"
    }
    host_url = f"https://graph.facebook.com/v8.0/{media_id}/insights"
    data = requests.get(host_url, params=params, headers=headers)
    resp = data.json()
    print(resp)
    data = dict()
    for metric in resp["data"]:
        data[metric["name"]] = metric["values"][0]["value"]
    if media_type == "a":
        cleaned_data = dict()
        for k in data:
            if k.startswith("carousel_album_"):
                cleaned_data[k[len("carousel_album_"):]] = data[k]
            else:
                cleaned_data[k] = data[k]
                # del data[k]
        data = cleaned_data
    try:
        body = data
        return body
    except Exception as e:
        return {"error": str(e)}
