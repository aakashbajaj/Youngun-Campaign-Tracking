import requests
from django.conf import settings

def send_scheduler_req():    
    header = {"token": settings.SC_API_TOKEN}
    resp = requests.get("http://13.126.72.48/scheduler", headers=header)
    if resp.status_code == 200:
        return resp.json()
    else:
        raise Exception