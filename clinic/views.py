from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response

from clinic.models import Clinic
from clinic.apps import INFO
from clinic.serializers import CreateClinicSerializer


class CreateClinic(generics.CreateAPIView):
    queryset = Clinic.objects.all()
    # permission_classes = (IsAuthenticated, IsAdminUser,)

    def create(self, request, *args, **kwargs):
        # INFO("[%s]CreateClinic: Clinic details [%s]", request.user.username, request.data)

        # Django rest_framework [DRF]: set of tools and utilities to help developers create RESTful APIs
        # quickly and efficiently. Serialization: DRF allows you to serialize and deserialize Django model
        # instances and querysets into JSON. Serializers in DRF provide a convenient way to convert complex data types,
        # such as querysets and model instances, into native Python datatypes that can be easily rendered into
        # JSON or other content types.
        serializer = CreateClinicSerializer(data=request.data, context={'request': request}, many=False)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

