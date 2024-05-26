from django.contrib.auth.models import AbstractUser, BaseUserManager, Permission
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
from django.utils.translation import gettext_lazy as _

class CustomUserManager(BaseUserManager):
    def create_user(self, username, email=None, password=None, **extra_fields):
        if not username:
            raise ValueError('The Username field must be set')
        username = self.model.normalize_username(username)
        extra_fields.setdefault('email', email)
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(username, email, password, **extra_fields)

class AppUser(AbstractUser):
    
    def save(self, *args, **kwargs):
        if self.pk:
            self.is_staff = True
            self.user_permissions.add(Permission.objects.get(codename="can_assign_helpers"))
        super().save(*args, **kwargs)
    
    objects = CustomUserManager()

    class Meta:
        permissions = [
            ('can_assign_helpers', _('Can Assign Helpers to Customers')),
        ]

    def __str__(self):
        return self.username

