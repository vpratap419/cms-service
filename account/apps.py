from django.apps import AppConfig
import logging

logger = logging.getLogger('django.account')
INFO = logger.info
ERROR = logger.error


class AccountConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'account'
