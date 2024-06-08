from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response

from registration.models import Registration

from clinic.apps import INFO
from registration.serializers import CreateRegistrationSerializer, RegistrationListSerializer, UpdateRegistrationSerializer, \
    DeleteRegistrationSerializer
from rest_framework.exceptions import NotFound


class CreateRegistration(generics.CreateAPIView):
    queryset = Registration.objects.all()

    # permission_classes = (IsAuthenticated, IsAdminUser,)

    def create(self, request, *args, **kwargs):
        # INFO("[%s]CreateRegistration: Registration details [%s]", request.user.username, request.data)

        # Django rest_framework [DRF]: set of tools and utilities to help developers create RESTful APIs
        # quickly and efficiently. Serialization: DRF allows you to serialize and deserialize Django model
        # instances and query sets into JSON. Serializers in DRF provide a convenient way to convert complex data types,
        # such as query sets and model instances, into native Python datatypes that can be easily rendered into
        # JSON or other content types.
        serializer = CreateRegistrationSerializer(data=request.data, context={'request': request}, many=False)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class GetRegistrations(generics.ListAPIView):
    queryset = Registration.objects.all()

    serializer_class = RegistrationListSerializer


class UpdateRegistration(generics.UpdateAPIView):
    serializer_class = UpdateRegistrationSerializer

    def update(self, request, *args, **kwargs):
        # INFO("[%s]UpdateRegistration:username[%s]",request.user.school.name, request.user.username)

        try:
            registration = Registration.objects.get(rid=kwargs['rid'])
        except Registration.DoesNotExist:
            raise NotFound({"message": "Registration with registration id '" + kwargs['rid'] + "' not found !"})

        serializer = self.get_serializer(registration, data=request.data, context={'request': request}, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data, status=status.HTTP_200_OK)


class DeleteRegistration(generics.DestroyAPIView):
    serializer_class = DeleteRegistrationSerializer

    def delete(self, request, *args, **kwargs):

        try:
            registration = Registration.objects.get(rid=kwargs['rid'])
        except Registration.DoesNotExist:
            raise NotFound({"message": "Registration with rid '" + kwargs['rid'] + "' not found !"})

        serializer = self.get_serializer(registration, data=request.data, context={'request': request}, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_destroy(instance=registration)
        return Response(serializer.data, status=status.HTTP_200_OK)

