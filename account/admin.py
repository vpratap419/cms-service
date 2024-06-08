from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from django.contrib.auth.models import Group
from account.models import User
from account.models import Doctor, Patient, Staff


class CustomUserAdmin(UserAdmin):  # GuardedModelAdmin
    model = User

    list_display = ('username', 'uid', 'role', 'cid', 'is_staff',
                    'name', 'gender', 'email', 'mobile', 'dob', 'addr', 'city', 'state', 'pin')  # Set list_filter to
    # activate filters in the main page of userslist
    list_filter = ('cid', 'role', 'is_staff',
                   'is_active',)  # Set list_filter to activate filters in the right sidebar of the change list page
    # of the admin
    fieldsets = (  # for fields to be used in editing users
        ('Personal Info',
         {'fields': ('cid', 'role', 'username', 'password', 'name', 'email', 'gender', 'mobile', 'dob', 'addr',
                     'city', 'state', 'pin')}),
        ('Permissions', {'fields': ('is_active', 'is_staff')}),
        ('Preferences', {'fields': ()}),
    )
    # InlineModelAdmin
    add_fieldsets = (  # for fields to be used when creating a user
        ('Personal Info', {
            'classes': ('wide',),
            'fields': (
                'cid', 'role', 'username', 'password1', 'password2', 'name', 'gender', 'email', 'mobile', 'dob', 'addr',
                'city', 'state', 'pin')}
         ),
        ('Permissions', {'fields': ('is_staff',)}),
        ('Preferences', {'fields': ()}),
    )

    search_fields = (
        'name',)  # Set search_fields to enable a search box on the admin change list page. This should be set to a
    # list of field names that will be searched whenever somebody typein
    ordering = ('username',)


admin.site.register(User, CustomUserAdmin)
admin.site.unregister(Group)


class DoctorAdmin(admin.ModelAdmin):
    list_display = ('did', 'specialization', 'degree', 'uid')


admin.site.register(Doctor, DoctorAdmin)


class PatientAdmin(admin.ModelAdmin):
    list_display = ('pid', 'aadhar', 'pan', 'emergency_contact', 'insurance', 'uid')


admin.site.register(Patient, PatientAdmin)


class StaffAdmin(admin.ModelAdmin):
    list_display = ('sid', 'uid')


admin.site.register(Staff, StaffAdmin)
