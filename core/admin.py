from django.contrib import admin
from . import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.admin import UserAdmin


@admin.register(models.BaseUser)
class BaseUserAdmin(UserAdmin):
    fieldsets = (
        (None, {"fields": ("password",)}),
        (
            _("Personal info"),
            {"fields": ("first_name", "second_name", "last_name", "date_of_birth", "gender", "email")}),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (_("Important dates"), {"fields": ("last_login",)}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "first_name", "second_name", "last_name", "date_of_birth", "gender", "email", "password1",
                    "password2",
                    "type"),
            },
        ),
    )
    list_display = ("email", "second_name", "first_name", "last_name", "is_staff")
    list_filter = ("is_staff", "is_superuser", "is_active", "groups", "type")
    search_fields = ("first_name", "last_name", "second_name", "email")
    ordering = ("date_joined",)
    filter_horizontal = (
        "groups",
        "user_permissions",
    )


@admin.register(models.Gym)
class GymAdmin(admin.ModelAdmin):
    list_display = ("name", "city", "address")


@admin.register(models.Schedule)
class ScheduleAdmin(admin.ModelAdmin):
    list_display = ("start_time", "end_time", "gym", "trainer")
