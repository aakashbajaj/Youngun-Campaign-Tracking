import boto3

from django.conf import settings

from datetime import timedelta
from django.utils import timezone
from django_q.tasks import async_task, schedule
from django_q.models import Schedule


def send_otp_mail(email, otptkn):
    msg = "Use the OTP: {0}".format(otptkn)
    subj = "Your login OTP for Youngun Portal"
    async_task('django.core.mail.send_mail', subj,
               msg, "support@youngun.in", [email])


def senf_otp_sms(mobile, otptkn):
    client = boto3.client(
        "sns",
        aws_access_key_id=settings.AWS_ACCESS_KEY,
        aws_secret_access_key=settings.AWS_SECRET,
        region_name=""
    )

    client.publish(
        PhoneNumber=mobile,
        msg="Youngun Portal OTP: {0}".format(otptkn),
        MessageAttributes={
            'AWS.SNS.SMS.SenderID': {
                'DataType': 'String',
                'StringValue': settings.SENDER_ID
            }
        }
    )
