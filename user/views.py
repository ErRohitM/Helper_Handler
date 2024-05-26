from django.shortcuts import render,redirect
from django.http import JsonResponse
from labour.models import Helpers
from customer.models import Customer
import json
from . forms import LoginForm
from django.contrib.auth import authenticate, login
from customer.decorators import user_operator, user_admin




def index(request):
    return render(request, 'index.html')


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            # print(username, password)
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user) 
                if not user.is_superuser: 
                    return redirect('assign_helpers')
                else:
                    return redirect('list_customers')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})


@user_operator("user.can_assign_helpers")
def assign_helpers(request):
    helpers_need_assign = Helpers.objects.filter(is_assigned=False)
    all_customers = Customer.objects.all()
    context = {
        'helpers_need_assign':helpers_need_assign,
        'all_customers':all_customers
    }
        
    return render(request, 'assign_helpers.html', context)

def save_selected_value(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON data'}, status=400)
        
        customer_id = data.get('customer_id')
        selected_value = data.get('selected_value')
        if not customer_id or not selected_value:
            return JsonResponse({'error': 'Missing required fields'}, status=400)   
        elif not Customer.objects.filter(id=customer_id).exists():
            return JsonResponse({'error': 'Invalid customer ID'}, status=400)
        else:
            customer = Customer.objects.get(id=customer_id)
            helper = Helpers.objects.get(id=selected_value) 
            if helper.is_assigned != True:
                customer.assigned_helper = helper
                helper.is_assigned = True
                customer.save()
                helper.save()
            else:
                return JsonResponse({'error': 'Customer is already assigned to a helper'}, status=400)
            
        return JsonResponse({'success': True})
    else:
        return JsonResponse({'success': False, 'error': 'Invalid request method'})
    



@user_admin()
def helper_assigned(request):
    helpers_assigned = Helpers.objects.all
    context = {
        'helpers_not_assigned': helpers_assigned,
    }
    return render(request, 'helper_assigned.html', context)
helper_not_assigned = Helpers.objects.filter(is_assigned=False)

