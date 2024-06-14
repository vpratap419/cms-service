from django.urls import path

# local imports
from emr import views

urlpatterns = [
    path('emr/create-medical history/', views.CreateMedicalHistory.as_view(), name='create-medical history'),
    path('emr/get-medical histories/', views.GetMedicalHistories.as_view(), name='get-medical histories'),
    path('emr/update-medical history/<int:mhid>/', views.UpdateMedicalHistory.as_view(), name='update-medical history'),
    path('emr/delete-medical history/<int:mhid>/', views.DeleteMedicalHistory.as_view(), name='delete-medical history'),

    path('emr/create-prescription/', views.CreatePrescription.as_view(), name='create-prescription'),
    path('emr/get-prescriptions/', views.GetPrescriptions.as_view(), name='get-prescriptions'),
    path('emr/update-prescription/<int:prid>/', views.UpdatePrescription.as_view(), name='update-prescription'),
    path('emr/delete-prescription/<int:prid>/', views.DeletePrescription.as_view(), name='delete-prescription'),

    path('emr/create-testreport/', views.CreateTestReport.as_view(), name='create-testreport'),
    path('emr/get-testreports/', views.GetTestReports.as_view(), name='get-testreports'),
    path('emr/update-testreport/<int:trid>/', views.UpdateTestReport.as_view(), name='update-testreport'),
    path('emr/delete-testreport/<int:trid>/', views.DeleteTestReport.as_view(), name='delete-testreport'),

    path('emr/create-medication/', views.CreateMedication.as_view(), name='create-medication'),
    path('emr/get-medications/', views.GetMedications.as_view(), name='get-medications'),
    path('emr/update-medication/<int:mid>/', views.UpdateMedication.as_view(), name='update-medication'),
    path('emr/delete-medication/<int:mid>/', views.DeleteMedication.as_view(), name='delete-medication'),
]
