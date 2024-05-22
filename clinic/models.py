from django.db import models


# Create your models here.
class Clinic(models.Model):
    cid = models.AutoField(primary_key=True)
    name = models.CharField("Clinic Name", max_length=128)
    contact = models.CharField("Clinic Contact", max_length=128)
    address = models.CharField("Clinic Address", max_length=1024)
    geolocation = models.CharField("Clinic Geolocation", max_length=128)
    website = models.CharField("Clinic Website", max_length=264)
    created = models.DateTimeField("Clinic Created", auto_now_add=True)
    updated = models.DateTimeField("Clinic updated", auto_now_add=True)

    objects = models.Manager()

    class Meta:
        verbose_name = 'Clinic'
        verbose_name_plural = 'Clinics'
