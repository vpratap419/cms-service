from django.urls import path

# local imports
from account import views

urlpatterns = [
    path('account/create-doctor/', views.CreateDoctor.as_view(), name='create-doctor'),
    path('account/get-doctors/', views.GetDoctors.as_view(), name='get-doctors'),
    path('account/update-doctor/<int:did>/', views.UpdateDoctor.as_view(), name='update-doctor'),
    path('account/delete-doctor/<int:did>/', views.DeleteDoctor.as_view(), name='delete-doctor'),
]
