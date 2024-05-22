from django.urls import path

# local imports
from clinic import views

urlpatterns = [
    path('clinic/create-clinic/', views.CreateClinic.as_view(), name='create-clinic'),
    path('clinic/get-clinics/', views.GetClinics.as_view(), name='get-clinics'),
    path('clinic/update-clinic/<int:cid>/', views.UpdateClinic.as_view(), name='update-clinic'),
    path('clinic/delete-clinic/<int:cid>/', views.DeleteClinic.as_view(), name='delete-clinic'),
]
