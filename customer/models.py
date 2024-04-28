from django.db import models
from django.contrib.auth.models import User
from labour.models import Helpers


class Customer(models.Model):
    # customer_name = models.ForeignKey(User, on_delete=models.CASCADE)
    customer_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    address = models.CharField(max_length=100)
    assigned_helper = models.OneToOneField(Helpers, on_delete = models.CASCADE, null = True, blank = True)
    phone = models.CharField(max_length=10, blank=True)
    
    def save(self, *args, **kwargs):
        super(Customer, self).save(*args, **kwargs)

    def __str__(self):
        return self.customer_name
    
