from django.shortcuts import render
from django.http import HttpResponse
from .models import Customer
from .forms import CustomerForm



def create_customer(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('Customer created successfully.')
        else:
            return HttpResponse('Invalid form data.')
    else:
        form = CustomerForm()
        return render(request, 'create_customer_profile.html', {'form': form})
    
    
def list_customers(request):
    customers = Customer.objects.all()
    return render(request, 'list_customers.html', {'customers': customers})
