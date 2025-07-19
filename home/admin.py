from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUserModel


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUserModel
    list_display = ("email", "is_staff", "is_active",)
    list_filter = ("email", "is_staff", "is_active",)
    fieldsets = (
        ('Information', {"fields": ("email", "password")}),
        ("Permissions", {"fields": ("is_superuser","is_staff", "is_active", "groups", "user_permissions")}),
    )
    add_fieldsets = (
        ("Add Information", {
            "classes": ("wide",),
            "fields": (
                "email", "password1", "password2", "is_staff",
                "is_active", "is_superuser" ,"groups", "user_permissions"
            )}
        ),
    )
    search_fields = ("email",)
    ordering = ("email",)
    
admin.site.register(CustomUserModel, CustomUserAdmin)