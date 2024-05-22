from rest_framework import serializers

# local imports
from clinic.models import Clinic
from clinic.apps import INFO


class CreateClinicSerializer(serializers.ModelSerializer):

    # You have more control before writing the data to DB using DRF. You have added or update custom values
    def create(self, data):
        INFO("[%s]CreateClinicSerializer: Data [%s]", data)
        return super(CreateClinicSerializer, self).create(data)

    class Meta:
        model = Clinic
        fields = ['cid', 'name', 'contact', 'address', 'geolocation', 'website']


class ClinicListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clinic
        fields = ['cid', 'name', 'contact', 'address', 'geolocation', 'website']


class UpdateClinicSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        return super(UpdateClinicSerializer, self).create(validated_data)

    class Meta:
        model = Clinic
        fields = ['cid', 'name', 'contact', 'address', 'geolocation', 'website']


class DeleteClinicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clinic
        fields = ['name', 'contact', 'address', 'geolocation', 'website']
