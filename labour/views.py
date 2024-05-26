from django.shortcuts import render, redirect
from .forms import Add_helper
from . models import Helpers
from customer.decorators import user_admin
from django.http import HttpResponse

@user_admin()
def add_helper(request):
    if request.method == 'POST':
        form = Add_helper(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Helper Created Sucessfully")
        else:
            return redirect('add_helper')
    else:
        form = Add_helper()
        return render(request, 'create_helper_profile.html', {'form': form})
    
@user_admin()
def list_helpers(request):
    helpers = Helpers.objects.all()
    context = {
        'helpers': helpers
    }
    return render(request, 'list_helpers.html', context)



    
