from django.urls import path

# local imports
from clinic import views

urlpatterns = [
    path('clinic/create-clinic/', views.CreateClinic.as_view(), name='create-clinic'),
]
