from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from .models import User


class UserInfoSerializer(ModelSerializer):
    token = serializers.CharField(source='token_string')

    class Meta:
        model = User
        fields = [
            'email',
            'token',
            'mobile',
        ]
