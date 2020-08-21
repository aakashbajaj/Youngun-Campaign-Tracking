from django.conf import settings

from datetime import timedelta
from django.utils import timezone
from django_q.tasks import async_task, schedule
from django_q.models import Schedule


def send_invite_mail(email, campaign_name, user_name):
    msg = "Hey!\n\nYou've been invited to view #{0} campaign by {1}.\n\nPlease login using your work mail ID on our portal https://tracking.youngun.in".format(
        campaign_name, user_name)
    subj = "{0} Meme Campaign Invite".format(campaign_name)
    async_task('django.core.mail.send_mail', subj,
               msg, "support@youngun.in", [email])
