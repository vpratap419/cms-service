from django.db import models
from account.models import Patient, Doctor

# Create your models here.

DAY = (
    ('Monday', 'MONDAY'),
    ('Tuesday', 'TUESDAY'),
    ('Wednesday', 'WEDNESDAY'),
    ('Thursday', 'THURSDAY'),
    ('Friday', 'FRIDAY'),
    ('Saturday', 'SATURDAY'),
    ('Sunday', 'SUNDAY'),
)


class Slot(models.Model):
    sid = models.AutoField(primary_key=True)
    did = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    slot_day = models.CharField("Slot Day", choices=DAY, max_length=100, null=True, blank=True)
    slot_time = models.TimeField("Slot Time", max_length=100, null=True, blank=True)
    created = models.DateTimeField("Slot Created", auto_now_add=True)
    updated = models.DateTimeField("Slot History Updated", auto_now_add=True)

    objects = models.Manager()

    class Meta:
        verbose_name = 'Slot'
        verbose_name_plural = 'Slots'

    def __str__(self):
        return '{} - {}'.format(self.sid, self.did)


STATUS = (
    ('Open', 'OPEN'),
    ('Booked', 'BOOKED'),
    ('Reserved', 'RESERVED')
)


class SlotCalendar(models.Model):
    scid = models.AutoField(primary_key=True)
    sid = models.ForeignKey(Slot, on_delete=models.CASCADE)
    slot_date = models.DateField("Slot Date", )
    slot_status = models.CharField("Slot Status", choices=STATUS, max_length=100, null=True, blank=True)
    created = models.DateTimeField("Slot Calendar Created", auto_now_add=True)
    updated = models.DateTimeField("Slot Calendar Updated", auto_now_add=True)

    objects = models.Manager()

    class Meta:
        verbose_name = 'Slot Calendar'
        verbose_name_plural = 'Slot Calendars'

    def __str__(self):
        return '{} - {}'.format(self.scid, self.sid)


class Appointment(models.Model):
    aid = models.AutoField(primary_key=True)
    scid = models.OneToOneField(SlotCalendar, on_delete=models.CASCADE)
    pid = models.ForeignKey(Patient, on_delete=models.CASCADE)
    created = models.DateTimeField("Appointment Created", auto_now_add=True)
    updated = models.DateTimeField("Appointment Updated", auto_now_add=True)

    objects = models.Manager()

    class Meta:
        verbose_name = 'Appointment'
        verbose_name_plural = 'Appointments'

    def __str__(self):
        return '{} - {}'.format(self.aid, self.scid)
