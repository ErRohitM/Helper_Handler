from functools import wraps
from django.http import HttpResponseForbidden
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth import REDIRECT_FIELD_NAME
from django.urls import reverse
from django.contrib import messages
from django.shortcuts import redirect

def user_operator(permission):
    def decorator(view_func):
        @wraps(view_func)
        def _wrapped_view(request, *args, **kwargs):
            if request.user.has_perm(permission):
                return view_func(request, *args, **kwargs)
            else:
                # return HttpResponseForbidden("You do not have permission to view this page. ")
                messages.error(request, "You do not have permission to view this page.")
                return redirect(f'{reverse("login")}?next={request.path}')
        return _wrapped_view
    return decorator

def user_admin(view_func=None, redirect_field_name=REDIRECT_FIELD_NAME,
                          login_url='login'):
    actual_decorator = user_passes_test(
        lambda u: u.is_superuser,
        login_url=login_url,
        redirect_field_name=redirect_field_name
    )
    if view_func:
        return actual_decorator(view_func)
    return actual_decorator
