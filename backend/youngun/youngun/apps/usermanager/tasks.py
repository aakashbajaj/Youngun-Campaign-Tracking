from django.conf import settings

from datetime import timedelta
from django.utils import timezone
from django_q.tasks import async_task, schedule
from django_q.models import Schedule


def send_invite_mail(email, campaign_name, user_name):
    msg = "Hi!\nYou've been invited to view a meme campaign by {0}.\nPlease login using your Email ID on https://tracking.youngun.in".format(
        user_name)
    subj = "{0} Meme Campaign Invite".format(campaign_name)
    async_task('django.core.mail.send_mail', subj,
               msg, "support@youngun.in", [email])
