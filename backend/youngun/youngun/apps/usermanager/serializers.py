from rest_framework.serializers import ModelSerializer

from .models import Organisation, Brand


class OrganisationSerializer(ModelSerializer):
    class Meta:
        model = Organisation
        fields = ['name']


class BrandSerializer(ModelSerializer):
    class Meta:
        model = Brand
        fields = ['name']
