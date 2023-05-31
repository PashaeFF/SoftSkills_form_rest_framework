from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.utils.translation import gettext_lazy as _
from django.utils.timezone import now


    
class User(AbstractUser):
    email = models.EmailField(max_length=200, unique=True, null=False, verbose_name=_("Email"))
    username = models.CharField(max_length=150, unique=True, verbose_name=_("Username"))
    fullname = models.CharField(max_length=150, null=False, verbose_name=_("Fullname"))
    password = models.CharField(max_length=500, null=False, verbose_name=_("Password"))
    company = models.BooleanField(default=True, verbose_name=_("Company"))
    last_login = models.DateTimeField(default=now, verbose_name=_("Last Login"))

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []