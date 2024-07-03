from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response

from appointment.models import Slot, SlotCalendar, Appointment

from clinic.apps import INFO
from appointment.serializers import (CreateSlotSerializer, SlotListSerializer,
                                     UpdateSlotSerializer, DeleteSlotSerializer)
from appointment.serializers import (CreateSlotCalendarSerializer, SlotCalendarListSerializer,
                                     UpdateSlotCalendarSerializer, DeleteSlotCalendarSerializer)
from appointment.serializers import (CreateAppointmentSerializer, AppointmentListSerializer,
                                     UpdateAppointmentSerializer, DeleteAppointmentSerializer)
from rest_framework.exceptions import NotFound


class CreateSlot(generics.CreateAPIView):
    queryset = Slot.objects.all()

    # permission_classes = (IsAuthenticated, IsAdminUser,)

    def create(self, request, *args, **kwargs):
        # INFO("[%s]CreateSlot: Slot details [%s]", request.user.username, request.data)

        # Django rest_framework [DRF]: set of tools and utilities to help developers create RESTful APIs
        # quickly and efficiently. Serialization: DRF allows you to serialize and deserialize Django model
        # instances and query sets into JSON. Serializers in DRF provide a convenient way to convert complex data types,
        # such as query sets and model instances, into native Python datatypes that can be easily rendered into
        # JSON or other content types.

        try:
            appointment = Slot.objects.get(did=request.data['did'])
        except Exception as e:
            print("Do nothing")
        else:
            raise NotFound({"message": "Doctor with doctor id '" + request.data['did'] + "' not found !"})

        serializer = CreateSlotSerializer(data=request.data, context={'request': request}, many=False)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class GetSlots(generics.ListAPIView):
    queryset = Slot.objects.all()

    serializer_class = SlotListSerializer


class UpdateSlot(generics.UpdateAPIView):
    serializer_class = UpdateSlotSerializer

    def update(self, request, *args, **kwargs):
        # INFO("[%s]UpdateSlot:username[%s]",request.user.school.name, request.user.username)

        try:
            appointment = Slot.objects.get(sid=kwargs['sid'])
        except Slot.DoesNotExist:
            raise NotFound({"message": "Slot with slot id '" + kwargs['sid'] + "' not found !"})

        serializer = self.get_serializer(appointment, data=request.data, context={'request': request}, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data, status=status.HTTP_200_OK)


class DeleteSlot(generics.DestroyAPIView):
    serializer_class = DeleteSlotSerializer

    def delete(self, request, *args, **kwargs):

        try:
            appointment = Slot.objects.get(sid=kwargs['sid'])
        except Slot.DoesNotExist:
            raise NotFound({"message": "Slot with sid '" + kwargs['sid'] + "' not found !"})

        serializer = self.get_serializer(appointment, data=request.data, context={'request': request}, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_destroy(instance=appointment)
        return Response(serializer.data, status=status.HTTP_200_OK)


class CreateSlotCalendar(generics.CreateAPIView):
    queryset = SlotCalendar.objects.all()

    # permission_classes = (IsAuthenticated, IsAdminUser,)

    def create(self, request, *args, **kwargs):
        # INFO("[%s]CreateSlotCalendar: SlotCalendar details [%s]", request.user.username, request.data)

        # Django rest_framework [DRF]: set of tools and utilities to help developers create RESTful APIs
        # quickly and efficiently. Serialization: DRF allows you to serialize and deserialize Django model
        # instances and query sets into JSON. Serializers in DRF provide a convenient way to convert complex data types,
        # such as query sets and model instances, into native Python datatypes that can be easily rendered into
        # JSON or other content types.

        try:
            appointment = SlotCalendar.objects.get(sid=request.data['sid'])
        except Exception as e:
            print("Do nothing")
        else:
            raise NotFound({"message": "Slot with slot id '" + request.data['sid'] + "' not found !"})

        serializer = CreateSlotCalendarSerializer(data=request.data, context={'request': request}, many=False)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class GetSlotCalendars(generics.ListAPIView):
    queryset = SlotCalendar.objects.all()

    serializer_class = SlotCalendarListSerializer


class UpdateSlotCalendar(generics.UpdateAPIView):
    serializer_class = UpdateSlotCalendarSerializer

    def update(self, request, *args, **kwargs):
        # INFO("[%s]UpdateSlotCalendar:username[%s]",request.user.school.name, request.user.username)

        try:
            appointment = SlotCalendar.objects.get(scid=kwargs['scid'])
        except SlotCalendar.DoesNotExist:
            raise NotFound({"message": "SlotCalendar with slotcalendar id '" + kwargs['scid'] + "' not found !"})

        serializer = self.get_serializer(appointment, data=request.data, context={'request': request}, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data, status=status.HTTP_200_OK)


class DeleteSlotCalendar(generics.DestroyAPIView):
    serializer_class = DeleteSlotCalendarSerializer

    def delete(self, request, *args, **kwargs):

        try:
            appointment = SlotCalendar.objects.get(scid=kwargs['scid'])
        except SlotCalendar.DoesNotExist:
            raise NotFound({"message": "SlotCalendar with scid '" + kwargs['scid'] + "' not found !"})

        serializer = self.get_serializer(appointment, data=request.data, context={'request': request}, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_destroy(instance=appointment)
        return Response(serializer.data, status=status.HTTP_200_OK)


class CreateAppointment(generics.CreateAPIView):
    queryset = Appointment.objects.all()

    # permission_classes = (IsAuthenticated, IsAdminUser,)

    def create(self, request, *args, **kwargs):
        # INFO("[%s]CreateAppointment: Appointment details [%s]", request.user.username, request.data)

        # Django rest_framework [DRF]: set of tools and utilities to help developers create RESTful APIs
        # quickly and efficiently. Serialization: DRF allows you to serialize and deserialize Django model
        # instances and query sets into JSON. Serializers in DRF provide a convenient way to convert complex data types,
        # such as query sets and model instances, into native Python datatypes that can be easily rendered into
        # JSON or other content types.

        try:
            appointment = Appointment.objects.get(scid=request.data['scid'])
        except Exception as e:
            print("Do nothing")
        else:
            raise NotFound({"message": "SlotCalendar with slotCalendar id '" + request.data['scid'] + "' not found !"})

        try:
            appointment = Appointment.objects.get(pid=request.data['pid'])
        except Exception as e:
            print("Do nothing")
        else:
            raise NotFound({"message": "Patient with patient id '" + request.data['pid'] + "' not found !"})

        serializer = CreateAppointmentSerializer(data=request.data, context={'request': request}, many=False)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class GetAppointments(generics.ListAPIView):
    queryset = Appointment.objects.all()

    serializer_class = AppointmentListSerializer


class UpdateAppointment(generics.UpdateAPIView):
    serializer_class = UpdateAppointmentSerializer

    def update(self, request, *args, **kwargs):
        # INFO("[%s]UpdateAppointment:username[%s]",request.user.school.name, request.user.username)

        try:
            appointment = Appointment.objects.get(aid=kwargs['aid'])
        except Appointment.DoesNotExist:
            raise NotFound({"message": "Appointment with appointment id '" + kwargs['aid'] + "' not found !"})

        serializer = self.get_serializer(appointment, data=request.data, context={'request': request}, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data, status=status.HTTP_200_OK)


class DeleteAppointment(generics.DestroyAPIView):
    serializer_class = DeleteAppointmentSerializer

    def delete(self, request, *args, **kwargs):

        try:
            appointment = Appointment.objects.get(aid=kwargs['aid'])
        except Appointment.DoesNotExist:
            raise NotFound({"message": "Appointment with aid '" + kwargs['aid'] + "' not found !"})

        serializer = self.get_serializer(appointment, data=request.data, context={'request': request}, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_destroy(instance=appointment)
        return Response(serializer.data, status=status.HTTP_200_OK)
