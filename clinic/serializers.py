from rest_framework import serializers

# local imports
from clinic.models import Clinic
from clinic.apps import INFO


class CreateClinicSerializer(serializers.ModelSerializer):

    # You have more control before writing the data to DB using DRF. You have add or update custom values
    def create(self, data):
        INFO("[%s]CreateClinicSerializer: Data [%s]", data)
        return super(CreateClinicSerializer, self).create(data)

    class Meta:
        model = Clinic
        fields = ['cid', 'name', 'contact', 'address', 'geolocation', 'website']

