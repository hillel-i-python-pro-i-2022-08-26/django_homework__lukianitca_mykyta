from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from apps.superuser_hw.models import User


class UserAdminCustom(UserAdmin):
    add_fieldsets = UserAdmin.add_fieldsets + (
        (
            None,
            {
                "fields": ("avatar",),
            },
        ),
    )
    fieldsets = UserAdmin.fieldsets + (("Extra Fields", {"fields": ("avatar",)}),)


admin.site.register(User, UserAdminCustom)
