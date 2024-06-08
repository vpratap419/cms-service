from django.db import models
from account.models import Patient, Doctor


# Create your models here.
class Registration(models.Model):
    rid = models.AutoField(primary_key=True)
    pid = models.OneToOneField(Patient, on_delete=models.CASCADE)
    did = models.ForeignKey(Doctor, verbose_name='Doctor', related_name="patient_doctor_registration",
                            on_delete=models.SET_NULL, null=True, blank=True)
    reason_for_visit = models.CharField("ReasonForVisit", max_length=100, null=True, blank=True)
    created = models.DateTimeField("Registration Created", auto_now_add=True)
    updated = models.DateTimeField("Registration updated", auto_now_add=True)

    objects = models.Manager()

    class Meta:
        verbose_name = 'Registration'
        verbose_name_plural = 'Registrations'

    def __str__(self):
        return '{} - {}'.format(self.rid, self.did)
