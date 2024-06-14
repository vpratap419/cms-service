from rest_framework import serializers

# local imports
from emr.models import MedicalHistory, Prescription, TestReport, Medication
from emr.apps import INFO


class CreateMedicalHistorySerializer(serializers.ModelSerializer):

    # You have more control before writing the data to DB using DRF. You have added or update custom values
    def create(self, data):
        INFO("[%s]CreateMedicalHistorySerializer: Data [%s]", data)
        return super(CreateMedicalHistorySerializer, self).create(data)

    class Meta:
        model = MedicalHistory
        fields = ['mhid', 'allergies', 'medications', 'surgeries', 'family_medical_history', 'life_style_factors',
                  'physical_examination', 'pid']


class MedicalHistoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicalHistory
        fields = ['mhid', 'allergies', 'medications', 'surgeries', 'family_medical_history', 'life_style_factors',
                  'physical_examination', 'pid']


class UpdateMedicalHistorySerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        return super(UpdateMedicalHistorySerializer, self).create(validated_data)

    class Meta:
        model = MedicalHistory
        fields = ['mhid', 'allergies', 'medications', 'surgeries', 'family_medical_history', 'life_style_factors',
                  'physical_examination', 'pid']


class DeleteMedicalHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicalHistory
        fields = ['mhid', 'allergies', 'medications', 'surgeries', 'family_medical_history', 'life_style_factors',
                  'physical_examination', 'pid']


class CreatePrescriptionSerializer(serializers.ModelSerializer):

    # You have more control before writing the data to DB using DRF. You have added or update custom values
    def create(self, data):
        INFO("[%s]CreatePrescriptionSerializer: Data [%s]", data)
        return super(CreatePrescriptionSerializer, self).create(data)

    class Meta:
        model = Prescription
        fields = ['prid', 'pid', 'did', 'prescription_date']


class PrescriptionListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prescription
        fields = ['prid', 'pid', 'did', 'prescription_date']


class UpdatePrescriptionSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        return super(UpdatePrescriptionSerializer, self).create(validated_data)

    class Meta:
        model = Prescription
        fields = ['prid', 'pid', 'did', 'prescription_date']


class DeletePrescriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prescription
        fields = ['prid', 'pid', 'did', 'prescription_date']


class CreateTestReportSerializer(serializers.ModelSerializer):

    # You have more control before writing the data to DB using DRF. You have added or update custom values
    def create(self, data):
        INFO("[%s]CreateTestReportSerializer: Data [%s]", data)
        return super(CreateTestReportSerializer, self).create(data)

    class Meta:
        model = TestReport
        fields = ['trid', 'prid', 'test_name', 'test_instruction', 'test_report']


class TestReportListSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestReport
        fields = ['trid', 'prid', 'test_name', 'test_instruction', 'test_report']


class UpdateTestReportSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        return super(UpdateTestReportSerializer, self).create(validated_data)

    class Meta:
        model = TestReport
        fields = ['trid', 'prid', 'test_name', 'test_instruction', 'test_report']


class DeleteTestReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestReport
        fields = ['trid', 'prid', 'test_name', 'test_instruction', 'test_report']


class CreateMedicationSerializer(serializers.ModelSerializer):

    # You have more control before writing the data to DB using DRF. You have added or update custom values
    def create(self, data):
        INFO("[%s]CreateMedicationSerializer: Data [%s]", data)
        return super(CreateMedicationSerializer, self).create(data)

    class Meta:
        model = Medication
        fields = ['mid', 'prid', 'medication_name', 'dosage_instruction', 'dosage']


class MedicationListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medication
        fields = ['mid', 'prid', 'medication_name', 'dosage_instruction', 'dosage']


class UpdateMedicationSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        return super(UpdateMedicationSerializer, self).create(validated_data)

    class Meta:
        model = Medication
        fields = ['mid', 'prid', 'medication_name', 'dosage_instruction', 'dosage']


class DeleteMedicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medication
        fields = ['mid', 'prid', 'medication_name', 'dosage_instruction', 'dosage']

