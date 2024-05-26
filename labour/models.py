from django.db import models
from PIL import Image
from phonenumber_field.modelfields import PhoneNumberField


class Helpers(models.Model):
    GENDER_CHOICES = (
        ("MALE", "MALE"),
        ("FEMALE", "FEMALE"),
        ("NOT_SPECIFIED", "NOT_SPECIFIED"),
    )

    helper = models.CharField(max_length=100)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    bio = models.TextField(max_length=500, blank=True)
    gender = models.CharField(max_length=15, choices = GENDER_CHOICES, blank=True)
    skill = models.CharField(max_length=100, blank=True)
    age = models.IntegerField(default=18)
    location = models.CharField(max_length=100, blank=True)
    phone = PhoneNumberField(null=False, blank=False, unique=True)
    is_assigned = models.BooleanField(default=False)
    assigned_at = models.DateTimeField(auto_now_add=True)
    
    
    
    def __str__(self):
        return self.helper
    
    
    

