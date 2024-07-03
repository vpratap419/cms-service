from rest_framework import serializers

# local imports
from appointment.models import Slot, SlotCalendar, Appointment
from appointment.apps import INFO


class CreateSlotSerializer(serializers.ModelSerializer):

    # You have more control before writing the data to DB using DRF. You have added or update custom values
    def create(self, data):
        INFO("[%s]CreateSlotSerializer: Data [%s]", data)
        return super(CreateSlotSerializer, self).create(data)

    class Meta:
        model = Slot
        fields = ['sid', 'did', 'slot_day', 'slot_time']


class SlotListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Slot
        fields = ['sid', 'did', 'slot_day', 'slot_time']


class UpdateSlotSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        return super(UpdateSlotSerializer, self).create(validated_data)

    class Meta:
        model = Slot
        fields = ['sid', 'did', 'slot_day', 'slot_time']


class DeleteSlotSerializer(serializers.ModelSerializer):
    class Meta:
        model = Slot
        fields = ['sid', 'did', 'slot_day', 'slot_time']


class CreateSlotCalendarSerializer(serializers.ModelSerializer):

    # You have more control before writing the data to DB using DRF. You have added or update custom values
    def create(self, data):
        INFO("[%s]CreateSlotCalendarSerializer: Data [%s]", data)
        return super(CreateSlotCalendarSerializer, self).create(data)

    class Meta:
        model = SlotCalendar
        fields = ['scid', 'sid', 'slot_date', 'slot_status']


class SlotCalendarListSerializer(serializers.ModelSerializer):
    class Meta:
        model = SlotCalendar
        fields = ['scid', 'sid', 'slot_date', 'slot_status']


class UpdateSlotCalendarSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        return super(UpdateSlotCalendarSerializer, self).create(validated_data)

    class Meta:
        model = SlotCalendar
        fields = ['scid', 'sid', 'slot_date', 'slot_status']


class DeleteSlotCalendarSerializer(serializers.ModelSerializer):
    class Meta:
        model = SlotCalendar
        fields = ['scid', 'sid', 'slot_date', 'slot_status']


class CreateAppointmentSerializer(serializers.ModelSerializer):

    # You have more control before writing the data to DB using DRF. You have added or update custom values
    def create(self, data):
        INFO("[%s]CreateAppointmentSerializer: Data [%s]", data)
        return super(CreateAppointmentSerializer, self).create(data)

    class Meta:
        model = Appointment
        fields = ['aid', 'scid', 'pid']


class AppointmentListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = ['aid', 'scid', 'pid']


class UpdateAppointmentSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        return super(UpdateAppointmentSerializer, self).create(validated_data)

    class Meta:
        model = Appointment
        fields = ['aid', 'scid', 'pid']


class DeleteAppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = ['aid', 'scid', 'pid']


