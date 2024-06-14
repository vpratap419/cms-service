from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response

from emr.models import MedicalHistory, Prescription, TestReport, Medication

from clinic.apps import INFO
from emr.serializers import (CreateMedicalHistorySerializer, MedicalHistoryListSerializer,
                             UpdateMedicalHistorySerializer, DeleteMedicalHistorySerializer)
from emr.serializers import (CreatePrescriptionSerializer, PrescriptionListSerializer,
                             UpdatePrescriptionSerializer, DeletePrescriptionSerializer)
from emr.serializers import (CreateTestReportSerializer, TestReportListSerializer,
                             UpdateTestReportSerializer, DeleteTestReportSerializer)
from emr.serializers import (CreateMedicationSerializer, MedicationListSerializer,
                             UpdateMedicationSerializer, DeleteMedicationSerializer)
from rest_framework.exceptions import NotFound


class CreateMedicalHistory(generics.CreateAPIView):
    queryset = MedicalHistory.objects.all()

    # permission_classes = (IsAuthenticated, IsAdminUser,)

    def create(self, request, *args, **kwargs):
        # INFO("[%s]CreateRegistration: Registration details [%s]", request.user.username, request.data)

        # Django rest_framework [DRF]: set of tools and utilities to help developers create RESTful APIs
        # quickly and efficiently. Serialization: DRF allows you to serialize and deserialize Django model
        # instances and query sets into JSON. Serializers in DRF provide a convenient way to convert complex data types,
        # such as query sets and model instances, into native Python datatypes that can be easily rendered into
        # JSON or other content types.

        try:
            emr = MedicalHistory.objects.get(pid=request.data['pid'])
        except Exception as e:
            print("Do nothing")
        else:
            raise NotFound({"message": "Medical History with patient id '" + request.data['pid'] + "' not found !"})

        serializer = CreateMedicalHistorySerializer(data=request.data, context={'request': request}, many=False)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class GetMedicalHistories(generics.ListAPIView):
    queryset = MedicalHistory.objects.all()

    serializer_class = MedicalHistoryListSerializer


class UpdateMedicalHistory(generics.UpdateAPIView):
    serializer_class = UpdateMedicalHistorySerializer

    def update(self, request, *args, **kwargs):
        # INFO("[%s]UpdateMedicalHistory:username[%s]",request.user.school.name, request.user.username)

        try:
            emr = MedicalHistory.objects.get(mhid=kwargs['mhid'])
        except MedicalHistory.DoesNotExist:
            raise NotFound({"message": "MedicalHistory with medical history id '" + kwargs['mhid'] + "' not found !"})

        serializer = self.get_serializer(emr, data=request.data, context={'request': request}, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data, status=status.HTTP_200_OK)


class DeleteMedicalHistory(generics.DestroyAPIView):
    serializer_class = DeleteMedicalHistorySerializer

    def delete(self, request, *args, **kwargs):

        try:
            emr = MedicalHistory.objects.get(mhid=kwargs['mhid'])
        except MedicalHistory.DoesNotExist:
            raise NotFound({"message": "MedicalHistory with mhid '" + kwargs['mhid'] + "' not found !"})

        serializer = self.get_serializer(emr, data=request.data, context={'request': request}, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_destroy(instance=emr)
        return Response(serializer.data, status=status.HTTP_200_OK)


class CreatePrescription(generics.CreateAPIView):
    queryset = Prescription.objects.all()

    # permission_classes = (IsAuthenticated, IsAdminUser,)

    def create(self, request, *args, **kwargs):
        # INFO("[%s]CreatePrescription: Prescription details [%s]", request.user.username, request.data)

        # Django rest_framework [DRF]: set of tools and utilities to help developers create RESTful APIs
        # quickly and efficiently. Serialization: DRF allows you to serialize and deserialize Django model
        # instances and query sets into JSON. Serializers in DRF provide a convenient way to convert complex data types,
        # such as query sets and model instances, into native Python datatypes that can be easily rendered into
        # JSON or other content types.

        try:
            emr = Prescription.objects.get(pid=request.data['pid'])
        except Exception as e:
            print("Do nothing")
        else:
            raise NotFound({"message": "Prescription with patient id '" + request.data['pid'] + "' not found !"})

        try:
            emr = Prescription.objects.get(did=request.data['did'])
        except Exception as e:
            print("Do nothing")
        else:
            raise NotFound({"message": "Prescription with doctor id '" + request.data['did'] + "' not found !"})

        serializer = CreatePrescriptionSerializer(data=request.data, context={'request': request}, many=False)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class GetPrescriptions(generics.ListAPIView):
    queryset = Prescription.objects.all()

    serializer_class = PrescriptionListSerializer


class UpdatePrescription(generics.UpdateAPIView):
    serializer_class = UpdatePrescriptionSerializer

    def update(self, request, *args, **kwargs):
        # INFO("[%s]UpdatePrescription:username[%s]",request.user.school.name, request.user.username)

        try:
            emr = Prescription.objects.get(prid=kwargs['prid'])
        except Prescription.DoesNotExist:
            raise NotFound({"message": "Prescription with prescription id '" + kwargs['prid'] + "' not found !"})

        serializer = self.get_serializer(emr, data=request.data, context={'request': request}, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data, status=status.HTTP_200_OK)


class DeletePrescription(generics.DestroyAPIView):
    serializer_class = DeletePrescriptionSerializer

    def delete(self, request, *args, **kwargs):

        try:
            emr = Prescription.objects.get(prid=kwargs['prid'])
        except Prescription.DoesNotExist:
            raise NotFound({"message": "Prescription with prid '" + kwargs['prid'] + "' not found !"})

        serializer = self.get_serializer(emr, data=request.data, context={'request': request}, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_destroy(instance=emr)
        return Response(serializer.data, status=status.HTTP_200_OK)


class CreateTestReport(generics.CreateAPIView):
    queryset = TestReport.objects.all()

    # permission_classes = (IsAuthenticated, IsAdminUser,)

    def create(self, request, *args, **kwargs):
        # INFO("[%s]CreateTestReport: TestReport details [%s]", request.user.username, request.data)

        # Django rest_framework [DRF]: set of tools and utilities to help developers create RESTful APIs
        # quickly and efficiently. Serialization: DRF allows you to serialize and deserialize Django model
        # instances and query sets into JSON. Serializers in DRF provide a convenient way to convert complex data types,
        # such as query sets and model instances, into native Python datatypes that can be easily rendered into
        # JSON or other content types.

        try:
            emr = TestReport.objects.get(prid=request.data['prid'])
        except Exception as e:
            print("Do nothing")
        else:
            raise NotFound({"message": "TestReport with prescription id '" + request.data['prid'] + "' not found !"})

        serializer = CreateTestReportSerializer(data=request.data, context={'request': request}, many=False)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class GetTestReports(generics.ListAPIView):
    queryset = TestReport.objects.all()

    serializer_class = TestReportListSerializer


class UpdateTestReport(generics.UpdateAPIView):
    serializer_class = UpdateTestReportSerializer

    def update(self, request, *args, **kwargs):
        # INFO("[%s]UpdateTestReport:username[%s]",request.user.school.name, request.user.username)

        try:
            emr = TestReport.objects.get(trid=kwargs['trid'])
        except TestReport.DoesNotExist:
            raise NotFound({"message": "TestReport with test report id '" + kwargs['trid'] + "' not found !"})

        serializer = self.get_serializer(emr, data=request.data, context={'request': request}, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data, status=status.HTTP_200_OK)


class DeleteTestReport(generics.DestroyAPIView):
    serializer_class = DeleteTestReportSerializer

    def delete(self, request, *args, **kwargs):

        try:
            emr = TestReport.objects.get(trid=kwargs['trid'])
        except TestReport.DoesNotExist:
            raise NotFound({"message": "TestReport with trid '" + kwargs['trid'] + "' not found !"})

        serializer = self.get_serializer(emr, data=request.data, context={'request': request}, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_destroy(instance=emr)
        return Response(serializer.data, status=status.HTTP_200_OK)


class CreateMedication(generics.CreateAPIView):
    queryset = Medication.objects.all()

    # permission_classes = (IsAuthenticated, IsAdminUser,)

    def create(self, request, *args, **kwargs):
        # INFO("[%s]CreateMedication: Medication details [%s]", request.user.username, request.data)

        # Django rest_framework [DRF]: set of tools and utilities to help developers create RESTful APIs
        # quickly and efficiently. Serialization: DRF allows you to serialize and deserialize Django model
        # instances and query sets into JSON. Serializers in DRF provide a convenient way to convert complex data types,
        # such as query sets and model instances, into native Python datatypes that can be easily rendered into
        # JSON or other content types.

        try:
            emr = Medication.objects.get(prid=request.data['prid'])
        except Exception as e:
            print("Do nothing")
        else:
            raise NotFound({"message": "Medication with prescription id '" + request.data['prid'] + "' not found !"})

        serializer = CreateMedicationSerializer(data=request.data, context={'request': request}, many=False)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class GetMedications(generics.ListAPIView):
    queryset = Medication.objects.all()

    serializer_class = MedicationListSerializer


class UpdateMedication(generics.UpdateAPIView):
    serializer_class = UpdateMedicationSerializer

    def update(self, request, *args, **kwargs):
        # INFO("[%s]UpdateMedication:username[%s]",request.user.school.name, request.user.username)

        try:
            emr = Medication.objects.get(mid=kwargs['mid'])
        except Medication.DoesNotExist:
            raise NotFound({"message": "Medication with medication id '" + kwargs['mid'] + "' not found !"})

        serializer = self.get_serializer(emr, data=request.data, context={'request': request}, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data, status=status.HTTP_200_OK)


class DeleteMedication(generics.DestroyAPIView):
    serializer_class = DeleteMedicationSerializer

    def delete(self, request, *args, **kwargs):

        try:
            emr = Medication.objects.get(mid=kwargs['mid'])
        except Medication.DoesNotExist:
            raise NotFound({"message": "Medication with mid '" + kwargs['mid'] + "' not found !"})

        serializer = self.get_serializer(emr, data=request.data, context={'request': request}, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_destroy(instance=emr)
        return Response(serializer.data, status=status.HTTP_200_OK)

