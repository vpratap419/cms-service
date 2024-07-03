from django.urls import path

# local imports
from appointment import views

urlpatterns = [
    path('appointment/create-slot/', views.CreateSlot.as_view(), name='create-slot'),
    path('appointment/get-slots/', views.GetSlots.as_view(), name='get-slots'),
    path('appointment/update-slot/<int:sid>/', views.UpdateSlot.as_view(), name='update-slot'),
    path('appointment/delete-slot/<int:sid>/', views.DeleteSlot.as_view(), name='delete-slot'),

    path('appointment/create-slotcalendar/', views.CreateSlotCalendar.as_view(), name='create-slotcalendar'),
    path('appointment/get-slotcalendars/', views.GetSlotCalendars.as_view(), name='get-slotcalendars'),
    path('appointment/update-slotcalendar/<int:scid>/', views.UpdateSlotCalendar.as_view(), name='update-slotcalendar'),
    path('appointment/delete-slotcalendar/<int:scid>/', views.DeleteSlotCalendar.as_view(), name='delete-slotcalendar'),

    path('appointment/create-appointment/', views.CreateAppointment.as_view(), name='create-appointment'),
    path('appointment/get-appointments/', views.GetAppointments.as_view(), name='get-appointments'),
    path('appointment/update-appointment/<int:aid>/', views.UpdateAppointment.as_view(), name='update-appointment'),
    path('appointment/delete-appointment/<int:aid>/', views.DeleteAppointment.as_view(), name='delete-appointment'),
]
