from django.db import models
from clinic.models import Clinic

Gender = (
    ('NA', 'NA'),
    ('Male', 'Male'),
    ('Female', 'Female'),
    ('Others', 'Others'),
)

Role = (
    ('NA', 'NA'),
    ('Patient', 'Patient'),
    ('Doctor', 'Doctor'),
    ('Other', 'Other'),
)


# Create your models here.
class User(models.Model):
    uid = models.AutoField(primary_key=True)
    cid = models.ForeignKey(Clinic, related_name="clinic_users",
                            on_delete=models.CASCADE, blank=True)
    first_name = models.CharField("User First Name", max_length=128)
    last_name = models.CharField("User Last Name", max_length=128)
    gender = models.CharField("Gender", choices=Gender, max_length=128, default='NA')
    u_name = models.CharField("User Name", max_length=200)
    password = models.CharField("Password", max_length=200)
    role = models.CharField("Role", choices=Role, max_length=128, default='NA')
    contact = models.CharField("User Contact", max_length=128)
    address = models.CharField("User Address", max_length=1024)
    email_address = models.CharField("User email", max_length=128)
    created = models.DateTimeField("Clinic Created", auto_now_add=True)
    updated = models.DateTimeField("Clinic updated", auto_now_add=True)

    objects = models.Manager()

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def __str__(self):
        return '{} - {} - {} - {}'.format(self.uid, self.u_name, self.role, self.cid)

