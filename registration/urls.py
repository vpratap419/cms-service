from django.urls import path

# local imports
from registration import views

urlpatterns = [
    path('registration/create-registration/', views.CreateRegistration.as_view(), name='create-registration'),
    path('registration/get-registrations/', views.GetRegistrations.as_view(), name='get-registrations'),
    path('registration/update-registration/<int:rid>/', views.UpdateRegistration.as_view(), name='update-registration'),
    path('registration/delete-registration/<int:rid>/', views.DeleteRegistration.as_view(), name='delete-registration'),
]
