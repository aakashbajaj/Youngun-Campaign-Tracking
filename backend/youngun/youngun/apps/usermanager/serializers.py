from rest_framework.serializers import ModelSerializer
from rest_framework import serializers

from .models import Brand, Profile, ClientProfile


class BrandSerializer(ModelSerializer):
    class Meta:
        model = Brand
        fields = ['name']


class ProfileSerializer(ModelSerializer):
    token = serializers.CharField(source='user.token_string')
    email = serializers.CharField(source='user.email')
    mobile = serializers.CharField(source='user.mobile')

    class Meta:
        model = Profile
        fields = ['full_name', 'token', 'email', 'mobile']


class InvitedUserSerializer(ModelSerializer):
    email = serializers.CharField(source='user.email')
    mobile = serializers.CharField(source='user.mobile')

    class Meta:
        model = ClientProfile
        fields = ['full_name', 'email', 'mobile']
