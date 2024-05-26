from django.db import models
from labour.models import Helpers
from phonenumber_field.modelfields import PhoneNumberField

class Customer(models.Model):
    customer_name = models.CharField(max_length=100, null=False, blank=False)
    email = models.EmailField(max_length=100)
    address = models.CharField(max_length=100)
    assigned_helper = models.OneToOneField(Helpers, on_delete = models.CASCADE, null = True, blank = True)
    phone = PhoneNumberField(null=False, blank=False, unique=True)


    def save(self, *args, **kwargs):
        super(Customer, self).save(*args, **kwargs)

    def __str__(self):
        return self.customer_name
    

    


