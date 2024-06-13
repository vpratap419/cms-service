from django.apps import AppConfig
import logging

logger = logging.getLogger('django.emr')
INFO = logger.info
ERROR = logger.error


class EmrConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'emr'

