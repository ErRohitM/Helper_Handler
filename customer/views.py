from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Customer
from .forms import CustomerForm
from django.contrib.auth import authenticate, login, logout 
from .forms import LoginForm
from .decorators import superuser_required



@superuser_required()
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
    
@superuser_required()  
def list_customers(request):
    customers = Customer.objects.all()
    return render(request, 'list_customers.html', {'customers': customers})

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)    
                return redirect('list_customers')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})