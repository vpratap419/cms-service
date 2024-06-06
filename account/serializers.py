from rest_framework import serializers

# local imports
from account.models import Doctor
from account.apps import INFO


class CreateDoctorSerializer(serializers.ModelSerializer):

    # You have more control before writing the data to DB using DRF. You have added or update custom values
    def create(self, data):
        INFO("[%s]CreateDoctorSerializer: Data [%s]", data)
        return super(CreateDoctorSerializer, self).create(data)

    class Meta:
        model = Doctor
        fields = ['did', 'uid', 'specialization', 'degree']


class DoctorListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = ['did', 'uid', 'specialization', 'degree']


class UpdateDoctorSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        return super(UpdateDoctorSerializer, self).create(validated_data)

    class Meta:
        model = Doctor
        fields = ['did', 'uid', 'specialization', 'degree']


class DeleteDoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = ['did', 'uid', 'specialization', 'degree']
