from django.db import models
from django.contrib.auth.models import User
from labour.models import Helpers
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin



class Customer(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    password = models.CharField(max_length=50)
    # customer_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    address = models.CharField(max_length=100)
    assigned_helper = models.OneToOneField(Helpers, on_delete = models.CASCADE, null = True, blank = True)
    phone = models.CharField(max_length=10, blank=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)


    def is_staff_user(self):
        return self.is_staff == True
    
    def is_admin_user(self):
        return self.is_superuser == True
    

    # objects = CustomUserManager() 

    # USERNAME_FIELD = 'username'
    # # EMAIL_FIELD = 'email'
    # REQUIRED_FIELDS = []

    def save(self, *args, **kwargs):
        super(Customer, self).save(*args, **kwargs)

    def __str__(self):
        return self.username
    


