from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response

from account.models import Doctor

from account.apps import INFO
from account.serializers import CreateDoctorSerializer, DoctorListSerializer, UpdateDoctorSerializer, \
    DeleteDoctorSerializer
from rest_framework.exceptions import NotFound


class CreateDoctor(generics.CreateAPIView):
    queryset = Doctor.objects.all()

    # permission_classes = (IsAuthenticated, IsAdminUser,)

    def create(self, request, *args, **kwargs):
        # INFO("[%s]CreateClinic: Clinic details [%s]", request.user.username, request.data)

        # Django rest_framework [DRF]: set of tools and utilities to help developers create RESTful APIs
        # quickly and efficiently. Serialization: DRF allows you to serialize and deserialize Django model
        # instances and query sets into JSON. Serializers in DRF provide a convenient way to convert complex data types,
        # such as query sets and model instances, into native Python datatypes that can be easily rendered into
        # JSON or other content types.
        serializer = CreateDoctorSerializer(data=request.data, context={'request': request}, many=False)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class GetDoctors(generics.ListAPIView):
    queryset = Doctor.objects.all()

    serializer_class = DoctorListSerializer


class UpdateDoctor(generics.UpdateAPIView):
    serializer_class = UpdateDoctorSerializer

    def update(self, request, *args, **kwargs):
        # INFO("[%s]UpdateClinic:username[%s]",request.user.school.name, request.user.username)

        try:
            account = Doctor.objects.get(did=kwargs['did'])
        except Doctor.DoesNotExist:
            raise NotFound({"message": "Doctor with doctor id '" + kwargs['did'] + "' not found !"})

        serializer = self.get_serializer(account, data=request.data, context={'request': request}, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data, status=status.HTTP_200_OK)


class DeleteDoctor(generics.DestroyAPIView):
    serializer_class = DeleteDoctorSerializer

    def delete(self, request, *args, **kwargs):

        try:
            account = Doctor.objects.get(did=kwargs['did'])
        except Doctor.DoesNotExist:
            raise NotFound({"message": "Doctor with did '" + kwargs['did'] + "' not found !"})

        serializer = self.get_serializer(account, data=request.data, context={'request': request}, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_destroy(instance=account)
        return Response(serializer.data, status=status.HTTP_200_OK)

