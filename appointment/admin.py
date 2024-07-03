from django.contrib import admin
from appointment.models import Slot, SlotCalendar, Appointment


# Register your models here.
class SlotAdmin(admin.ModelAdmin):
    list_display = ('sid', 'did', 'slot_day', 'slot_time')


admin.site.register(Slot, SlotAdmin)


class SlotCalenderAdmin(admin.ModelAdmin):
    list_display = ('scid', 'sid', 'slot_date', 'slot_status')


admin.site.register(SlotCalendar, SlotCalenderAdmin)


class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('aid', 'scid', 'pid')


admin.site.register(Appointment, AppointmentAdmin)

