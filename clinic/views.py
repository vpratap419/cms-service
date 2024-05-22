from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response

from clinic.models import Clinic

from clinic.apps import INFO
from clinic.serializers import CreateClinicSerializer, ClinicListSerializer, UpdateClinicSerializer, \
    DeleteClinicSerializer
from rest_framework.exceptions import NotFound


class CreateClinic(generics.CreateAPIView):
    queryset = Clinic.objects.all()

    # permission_classes = (IsAuthenticated, IsAdminUser,)

    def create(self, request, *args, **kwargs):
        # INFO("[%s]CreateClinic: Clinic details [%s]", request.user.username, request.data)

        # Django rest_framework [DRF]: set of tools and utilities to help developers create RESTful APIs
        # quickly and efficiently. Serialization: DRF allows you to serialize and deserialize Django model
        # instances and query sets into JSON. Serializers in DRF provide a convenient way to convert complex data types,
        # such as query sets and model instances, into native Python datatypes that can be easily rendered into
        # JSON or other content types.
        serializer = CreateClinicSerializer(data=request.data, context={'request': request}, many=False)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class GetClinics(generics.ListAPIView):
    queryset = Clinic.objects.all()

    serializer_class = ClinicListSerializer


class UpdateClinic(generics.UpdateAPIView):
    serializer_class = UpdateClinicSerializer

    def update(self, request, *args, **kwargs):
        #INFO("[%s]UpdateClinic:username[%s]",request.user.school.name, request.user.username)

        try:
            clinic = Clinic.objects.get(cid=kwargs['cid'])
        except Clinic.DoesNotExist:
            raise NotFound({"message": "Clinic with clinic id '" + kwargs['cid'] + "' not found !"})

        serializer = self.get_serializer(clinic, data=request.data, context={'request': request}, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data, status=status.HTTP_200_OK)


class DeleteClinic(generics.DestroyAPIView):
    serializer_class = DeleteClinicSerializer

    def delete(self, request, *args, **kwargs):

        try:
            clinic = Clinic.objects.get(cid=kwargs['cid'])
        except Clinic.DoesNotExist:
            raise NotFound({"message": "Clinic with cid '" + kwargs['cid'] + "' not found !"})

        serializer = self.get_serializer(clinic, data=request.data, context={'request': request}, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_destroy(instance=clinic)
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
