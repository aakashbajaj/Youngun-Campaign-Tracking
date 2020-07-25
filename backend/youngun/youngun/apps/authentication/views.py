import random
import re
from datetime import datetime

from rest_framework import status
from rest_framework.generics import RetrieveAPIView
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from .tasks import send_otp_mail

from .models import User

from .serializers import UserInfoSerializer
from .renderers import UserInfoJSONRenderer

# Create your views here.


def generate_otp():
    return random.randint(100000, 999999)


def generate_tempid():
    return str(random.randint(1000, 9999))


class UserInfoRetrieveAPIView(RetrieveAPIView):
    permission_classes = (IsAuthenticated, )
    serializer_class = UserInfoSerializer
    renderer_classes = (UserInfoJSONRenderer, )

    def retrieve(self, request, *args, **kwargs):
        serializer = self.serializer_class(request.user)

        return Response(serializer.data, status=status.HTTP_200_OK)


class InitiateLogin(APIView):
    permission_classes = (AllowAny, )

    def post(self, request):

        try:
            email = request.data["email"]
        except KeyError:
            return Response({"response": "Invalid Email"}, status.HTTP_400_BAD_REQUEST)
        # verify email exists
        try:
            user_obj = User.objects.get(email=email)
        except User.DoesNotExist:
            return Response({"response": "Not Allowed. Invalid Email"}, status.HTTP_401_UNAUTHORIZED)

        # generate temp id for user
        # generate OTP
        # authInProgress = true
        tempid = generate_tempid()
        tempotp = generate_otp()

        user_obj.tempid = tempid
        user_obj.tempotp = tempotp
        user_obj.authInProgress = True
        user_obj.last_requested = datetime.now()

        # save instance
        user_obj.save()

        # send sms, mail
        # send_mail(
        #     subject="Your OTP for Youngun Portal",
        #     message="Use the OTP: {0}".format(
        #         tempotp),
        #     from_email="support@youngun.in",
        #     recipient_list=[user_obj.email],
        #     fail_silently=False
        # )
        send_otp_mail(user_obj.email, tempotp)
        print("OTP is " + str(tempotp))

        # return tempid, masked email/mobile
        masked_email = re.sub(r"([A-Za-z0-9])(.*)@([A-Za-z])(.*)\.(.*)$", lambda x: r"{}{}@{}{}.{}".format(
            x.group(1), "*"*len(x.group(2)), x.group(3), "*"*len(x.group(4)), x.group(5)), user_obj.email)
        if not user_obj.mobile == "":
            masked_mobile = user_obj.mobile[3:5] + \
                "*******" + user_obj.mobile[-2:]
        payload = {
            "tempid": tempid,
            "masked_email": masked_email,
            "masked_mobile": masked_mobile
        }

        return Response(payload, status=status.HTTP_200_OK)


class VerifyLogin(APIView):
    permission_classes = (AllowAny, )

    def post(self, request):
        try:
            tempid = request.data["tempid"]
            inpotp = request.data["inpotp"]

        except KeyError:
            return Response({"response": "Invalid Data"}, status.HTTP_400_BAD_REQUEST)

        # get user obj from temp id and email
        try:
            user_obj = User.objects.get(tempid=tempid)
        except User.DoesNotExist:
            return Response({"response": "Not Allowed. Invalid Request"}, status.HTTP_400_BAD_REQUEST)

        # verify if otp matches
        if inpotp == user_obj.tempotp:
            # authInProgress = false
            # destroy otp and tempid
            user_obj.authInProgress = False
            user_obj.tempid = None
            user_obj.tempotp = None
            user_obj.save()
        else:
            return Response({"response": "Incorrect OTP"}, status.HTTP_401_UNAUTHORIZED)

        # return token
        payload = {
            "token": user_obj.token_string
        }

        return Response(payload, status=status.HTTP_200_OK)
