from django.db import models
from django.contrib.auth.models import User
from labour.models import Helpers
from django.contrib.auth.models import AbstractUser, BaseUserManager



class CustomUserManager(BaseUserManager):
    def create_user(self, username, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(username=username.strip(), email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, customer_name, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(customer_name, password, **extra_fields)
    
class Customer(AbstractUser):
    # customer_name = models.ForeignKey(User, on_delete=models.CASCADE)
    customer_name = models.CharField(
        max_length=150, 
        unique=True,
        help_text='Required. 150 characters or fewer. Letters, digits, and spaces only.',
        validators=[],
        error_messages={
            'unique': "A user with that username already exists.",
        },
    )
    password = models.CharField(max_length=50)
    # customer_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    address = models.CharField(max_length=100)
    assigned_helper = models.OneToOneField(Helpers, on_delete = models.CASCADE, null = True, blank = True)
    phone = models.CharField(max_length=10, blank=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)


    def is_staff_user(self):
        return self.is_staff == True
    
    def is_admin_user(self):
        return self.is_admin == True
    
    objects = CustomUserManager()

    
    USERNAME_FIELD = 'customer_name'
    # EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = []
    def save(self, *args, **kwargs):
        super(Customer, self).save(*args, **kwargs)

    def __str__(self):
        return self.customer_name
    


