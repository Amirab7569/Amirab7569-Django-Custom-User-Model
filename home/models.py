from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from .managers import CustomUserManager
from django.utils import timezone


class CustomUserModel(AbstractUser):
    username = models.CharField( _("Username"), max_length=50)
    email = models.EmailField(_("Email Address"), unique=True)
    full_name = models.CharField(_("Full Name"), max_length=50)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)
    
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['full_name', 'username']

    objects = CustomUserManager()

    def __str__(self):
        return self.email
    
    
