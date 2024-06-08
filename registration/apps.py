from django.apps import AppConfig
import logging

logger = logging.getLogger('django.clinic')
INFO = logger.info
ERROR = logger.error


class RegistrationConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'registration'
