from django.contrib import admin
from emr.models import MedicalHistory


# Register your models here.
class MedicalHistoryAdmin(admin.ModelAdmin):
    list_display = ('mhid', 'allergies', 'medications', 'surgeries', 'family_medical_history', 'life_style_factors',
                    'pid')


admin.site.register(MedicalHistory, MedicalHistoryAdmin)
