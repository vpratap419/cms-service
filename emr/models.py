from django.db import models
from account.models import Patient, Doctor


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
        verbose_name = 'Medical History'
        verbose_name_plural = 'Medical Histories'

    def __str__(self):
        return '{} - {}'.format(self.mhid, self.pid)


class Prescription(models.Model):
    prid = models.AutoField(primary_key=True)
    pid = models.ForeignKey(Patient, on_delete=models.CASCADE)
    did = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    prescription_date = models.DateField("Prescription Date", auto_now_add=True)
    created = models.DateTimeField("Prescription Created", auto_now_add=True)
    updated = models.DateTimeField("Prescription Updated", auto_now_add=True)

    objects = models.Manager()

    class Meta:
        verbose_name = 'Prescription'
        verbose_name_plural = 'Prescriptions'

    def __str__(self):
        return '{} - {}'.format(self.prid, self.pid)


STATUS = (
    ('Pending', 'Pending'),
    ('Available', 'Available')
)


class TestReport(models.Model):
    trid = models.AutoField(primary_key=True)
    prid = models.ForeignKey(Prescription, on_delete=models.CASCADE)
    test_name = models.CharField("Test Name", max_length=100, null=True, blank=True)
    test_instruction = models.CharField("Test Instruction", max_length=100, null=True, blank=True)
    test_report = models.CharField("Test Report", choices=STATUS, max_length=100, null=True, blank=True)
    created = models.DateTimeField("Test Report Created", auto_now_add=True)
    updated = models.DateTimeField("Test Report Updated", auto_now_add=True)

    objects = models.Manager()

    class Meta:
        verbose_name = 'Test Report'
        verbose_name_plural = 'Test Reports'

    def __str__(self):
        return '{} - {}'.format(self.trid, self.prid)


DOSAGE = (
    ('Daily', 'Daily'),
    ('Weekly', 'Weekly')
)


class Medication(models.Model):
    mid = models.AutoField(primary_key=True)
    prid = models.ForeignKey(Prescription, on_delete=models.CASCADE)
    medication_name = models.CharField("Medication Name", max_length=100, null=True, blank=True)
    dosage_instruction = models.CharField("Dosage Instruction", max_length=100, null=True, blank=True)
    dosage = models.CharField("Dosage", choices=DOSAGE, max_length=100, null=True, blank=True)
    created = models.DateTimeField("Test Report Created", auto_now_add=True)
    updated = models.DateTimeField("Test Report Updated", auto_now_add=True)

    objects = models.Manager()

    class Meta:
        verbose_name = 'Medication'
        verbose_name_plural = 'Medications'

    def __str__(self):
        return '{} - {}'.format(self.mid, self.prid)

