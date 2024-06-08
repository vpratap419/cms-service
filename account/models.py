from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models

from account.managers import CustomUserManager
from clinic.models import Clinic

GENDER = (
    ('UNKNOWN', 'Unknown'),
    ('F', 'Female'),
    ('M', 'Male'),
)


class User(AbstractUser):
    # TODO:: Rename username field to mobile username (django user): Required. 150 characters or fewer. Usernames may
    #  contain alphanumeric, _, @, +, . and - characters. first_name (django user): Optional (blank=True). 30
    #  characters or fewer. last_name (django user): Optional (blank=True). 150 characters or fewer. password (django
    #  user): Required. A hash of, and metadata about, the password.

    ROLE = (
        ('ADMIN', 'Admin'),
        ('STAFF', 'Staff'),  # Guest Admin account is to support work to a specific school account
        ('DOCTOR', 'Doctor'),
        ('PATIENT', 'Patient'),
    )

    uid = models.AutoField(primary_key=True)
    # Relationships
    cid = models.ForeignKey(Clinic, verbose_name='Clinic', related_name="user_clinic",
                            on_delete=models.SET_NULL, null=True, blank=True)

    name = models.CharField("Name", max_length=80)
    role = models.CharField("Role", choices=ROLE, max_length=16)
    gender = models.CharField("Gender", choices=GENDER, max_length=16)
    email = models.EmailField("Email", null=True, blank=True)
    mobile = models.EmailField("Mobile", null=True, blank=True)
    dob = models.DateField("Date Of Birth", null=True, blank=True)
    addr = models.CharField("Address Line", max_length=100, null=True, blank=True)
    city = models.CharField("City", max_length=80, null=True, blank=True)
    state = models.CharField("State", max_length=60, null=True, blank=True)
    pin = models.IntegerField("Pin", null=True, blank=True)

    created = models.DateTimeField("Account Created", auto_now_add=True)

    REQUIRED_FIELDS = []  # Required to create an account

    objects = CustomUserManager()

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'

    def __str__(self):
        return self.username


class Doctor(models.Model):
    did = models.AutoField(primary_key=True)
    uid = models.OneToOneField(User, on_delete=models.CASCADE)
    specialization = models.CharField("Specialization", max_length=100, null=True, blank=True)
    degree = models.CharField("Degree", max_length=100, null=True, blank=True)
    created = models.DateTimeField("Doctor Created", auto_now_add=True)
    updated = models.DateTimeField("Doctor updated", auto_now_add=True)

    objects = models.Manager()

    class Meta:
        verbose_name = 'Doctor'
        verbose_name_plural = 'Doctors'

    def __str__(self):
        return '{} - {}'.format(self.did, self.uid)


class Patient(models.Model):
    pid = models.AutoField(primary_key=True)
    uid = models.OneToOneField(User, on_delete=models.CASCADE)
    aadhar = models.CharField("Aadhar", max_length=100, null=True, blank=True)
    pan = models.CharField("Pan", max_length=100, null=True, blank=True)
    emergency_contact = models.CharField("Contact", max_length=100, null=True, blank=True)
    insurance = models.CharField("Insurance", max_length=100, null=True, blank=True)
    created = models.DateTimeField("Patient Created", auto_now_add=True)
    updated = models.DateTimeField("Patient updated", auto_now_add=True)

    objects = models.Manager()

    class Meta:
        verbose_name = 'Patient'
        verbose_name_plural = 'Patients'

    def __str__(self):
        return '{} - {}'.format(self.pid, self.uid)