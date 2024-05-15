from django.apps import AppConfig
import logging

logger = logging.getLogger('django.clinic')
INFO = logger.info
ERROR = logger.error


class ClinicConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'clinic'
