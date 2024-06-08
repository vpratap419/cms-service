from rest_framework import serializers

# local imports
from registration.models import Registration
from registration.apps import INFO


class CreateRegistrationSerializer(serializers.ModelSerializer):

    # You have more control before writing the data to DB using DRF. You have added or update custom values
    def create(self, data):
        INFO("[%s]CreateRegistrationSerializer: Data [%s]", data)
        return super(CreateRegistrationSerializer, self).create(data)

    class Meta:
        model = Registration
        fields = ['rid', 'reason_for_visit', 'pid', 'did']


class RegistrationListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Registration
        fields = ['rid', 'reason_for_visit', 'pid', 'did']


class UpdateRegistrationSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        return super(UpdateRegistrationSerializer, self).create(validated_data)

    class Meta:
        model = Registration
        fields = ['rid', 'reason_for_visit', 'pid', 'did']


class DeleteRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Registration
        fields = ['rid', 'reason_for_visit', 'pid', 'did']
