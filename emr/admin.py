from django.contrib import admin
from emr.models import MedicalHistory, Prescription, TestReport, Medication


# Register your models here.
class MedicalHistoryAdmin(admin.ModelAdmin):
    list_display = ('mhid', 'allergies', 'medications', 'surgeries', 'family_medical_history', 'life_style_factors',
                    'physical_examination', 'pid')


admin.site.register(MedicalHistory, MedicalHistoryAdmin)


class PrescriptionAdmin(admin.ModelAdmin):
    list_display = ('prid', 'pid', 'did', 'prescription_date')


admin.site.register(Prescription, PrescriptionAdmin)


class TestReportAdmin(admin.ModelAdmin):
    list_display = ('trid', 'prid', 'test_name', 'test_instruction', 'test_report')


admin.site.register(TestReport, TestReportAdmin)


class MedicationAdmin(admin.ModelAdmin):
    list_display = ('mid', 'prid', 'medication_name', 'dosage_instruction', 'dosage')


admin.site.register(Medication, MedicationAdmin)

