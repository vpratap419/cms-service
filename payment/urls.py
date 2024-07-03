from django.urls import path

# local imports
from payment import views

urlpatterns = [
    path('payment/create-order/', views.CreateOrder.as_view(), name='create-order'),

]
