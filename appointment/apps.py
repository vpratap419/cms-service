from django.apps import AppConfig
import logging

logger = logging.getLogger('django.appointment')
INFO = logger.info
ERROR = logger.error


class AppointmentConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'appointment'
