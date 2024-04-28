from django.db import models
from PIL import Image

class Helpers(models.Model):
    # CUSTOMER_CHOICES = [(customer.id, str(customer)) for customer in customers]
    helper = models.CharField(max_length=100)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    bio = models.TextField(max_length=500, blank=True)
    gender = models.CharField(max_length=10, blank=True)
    skill = models.CharField(max_length=100, blank=True)
    age = models.IntegerField(default=18)
    location = models.CharField(max_length=100, blank=True)
    phone = models.CharField(max_length=10, blank=True)
    is_assigned = models.BooleanField(default=False)
    assigned_at = models.DateTimeField(auto_now_add=True)
    # selected_customer = models.IntegerField(choices=CUSTOMER_CHOICES, null=True, blank=True)
    # assigned_to = models.OneToOneField(Customer, on_delete=models.CASCADE, blank=True, null = True)

    def __str__(self):
        return self.helper
    
    # def get_image(self):
    #     if self.image:
    #         return 'http://127.0.0.1:8000' + self.image.url
    #     return ''
    
    

