import requests

from django.conf import settings


def get_business_discovery_user(username, next_token=None):
    self_ig_userid = settings.SELF_IG_USERID
    access_token = settings.INSTA_GRAPH_LL_TOKEN

    fields = f"business_discovery.username({username}){{media{{caption,media_type,permalink,comments_count,like_count,media_url,timestamp,children{{media_url,media_type}} }}}}"

    if next_token is not None:
        fields = f"business_discovery.username({username}){{media.after({next_token}){{caption,media_type,permalink,comments_count,like_count,media_url,timestamp,children{{media_url,media_type}} }}}}"
    
    params = {
        "fields": fields,
    }
    headers = {
        "Authorization": f"Bearer {access_token}"
    }

    host_url = f"https://graph.facebook.com/v8.0/{self_ig_userid}"

    data = requests.get(host_url, params=params, headers=headers)
    resp = data.json()

    try:
        body = resp["business_discovery"]
        return body
    except Exception as e:
        return {"error": str(e)}
