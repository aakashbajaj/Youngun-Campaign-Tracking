from rest_framework.serializers import ModelSerializer

from .models import Organisation, User


class OrganisationSerializer(ModelSerializer):
    class Meta:
        model = Organisation
        fields = ['name']


class UserInfoSerializer(ModelSerializer):
    organisation = OrganisationSerializer(read_only=True)

    class Meta:
        model = User
        fields = [
            'full_name',
            'email',
            'organisation',
            'token_string'
        ]
