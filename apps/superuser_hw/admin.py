from django.contrib import admin
from django.contrib.admin import ModelAdmin
from django.contrib.auth.admin import UserAdmin

from apps.superuser_hw.models import User, Request


class UserAdminCustom(UserAdmin):
    add_fieldsets = UserAdmin.add_fieldsets + (
        (
            None,
            {
                "fields": ("avatar",),
            },
        ),
    )
    fieldsets = UserAdmin.fieldsets + (
        (
            "Extra Fields",
            {"fields": ("avatar",)},
        ),
    )


class RequestAdmin(ModelAdmin):
    list_display = ("path", "session_key", "user")
    ordering = ("session_key",)
    readonly_fields = ("visits_count",)


admin.site.register(User, UserAdminCustom)
admin.site.register(Request, RequestAdmin)
