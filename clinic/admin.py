from django.contrib import admin
from clinic.models import Clinic


# Register your models here.
class ClinicAdmin(admin.ModelAdmin):
    list_display = ('cid', 'name', 'contact', 'address', 'geolocation', 'website')


admin.site.register(Clinic, ClinicAdmin)
