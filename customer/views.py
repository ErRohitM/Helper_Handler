from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Customer
from .forms import CustomerForm
from . decorators import user_admin



@user_admin()
def create_customer(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('Customer created successfully.')
        else:
            return redirect('create_customer')
    else:
        form = CustomerForm()
        return render(request, 'create_customer_profile.html', {'form': form})
    
@user_admin()  
def list_customers(request):
    customers = Customer.objects.all()
    return render(request, 'list_customers.html', {'customers': customers})

