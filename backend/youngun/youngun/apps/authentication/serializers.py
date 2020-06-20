from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from .models import Organisation, User


class OrganisationSerializer(ModelSerializer):
    class Meta:
        model = Organisation
        fields = ['name']


class UserInfoSerializer(ModelSerializer):
    organisation = OrganisationSerializer(read_only=True)
    token = serializers.CharField(source='token_string')

    class Meta:
        model = User
        fields = [
            'full_name',
            'email',
            'organisation',
            'token'
        ]
