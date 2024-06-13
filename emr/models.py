from django.db import models
from account.models import Patient


# Create your models here.
class MedicalHistory(models.Model):
    mhid = models.AutoField(primary_key=True)
    pid = models.OneToOneField(Patient, on_delete=models.CASCADE)
    allergies = models.CharField("Allergies", max_length=100, null=True, blank=True)
    medications = models.CharField("Medications", max_length=100, null=True, blank=True)
    surgeries = models.CharField("Surgeries", max_length=100, null=True, blank=True)
    family_medical_history = models.CharField("Family Medical History", max_length=100, null=True, blank=True)
    life_style_factors = models.CharField("Life Style Factor", max_length=100, null=True, blank=True)
    physical_examination = models.CharField("Physical Examination", max_length=100, null=True, blank=True)
    created = models.DateTimeField("Medical History Created", auto_now_add=True)
    updated = models.DateTimeField("Medical History Updated", auto_now_add=True)

    objects = models.Manager()

    class Meta:
        verbose_name = 'MedicalHistory'
        verbose_name_plural = 'MedicalHistories'

    def __str__(self):
        return '{} - {}'.format(self.mhid, self.pid)

