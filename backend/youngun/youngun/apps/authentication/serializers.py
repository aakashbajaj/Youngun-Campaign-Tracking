from rest_framework.serializers import ModelSerializer

from .models import Organisation, User


class OrganisationSerializer(ModelSerializer):
    class Meta:
        model = Organisation
        fields = ['name']
