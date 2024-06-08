from django.contrib import admin
from registration.models import Registration


# Register your models here.
class RegistrationAdmin(admin.ModelAdmin):
    list_display = ('rid', 'reason_for_visit', 'pid', 'did')


admin.site.register(Registration, RegistrationAdmin)
