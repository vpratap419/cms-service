from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _

from clinic.models import Clinic


class CustomUserManager(BaseUserManager):

    # def create_user(self, username, password, school, **extra_fields):
    #     if not username:
    #         raise ValueError(_('The Username must be set'))
    #     if not school:
    #         raise ValueError(_("School Id is required"))
    #     if not password:
    #         raise ValueError(_("Password is required"))
    #
    #     extra_fields.setdefault('is_active', True)
    #     school = School.objects.get(pk=school)
    #     user = self.model(username=username, school=school, **extra_fields)
    #     user.set_password(password)
    #     user.save()
    #     return user

    # creating superuser
    def create_superuser(self, username, password, **extra_fields):
        if not username:
            raise ValueError(_('The Username must be set'))
        if not password:
            raise ValueError(_("Password is required"))

        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save()
        return user
