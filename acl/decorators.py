from django.http import HttpResponse
from django.shortcuts import redirect
from django.contrib import messages


def allowed_users(allowed_roles=[]):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):
            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name
            if group in allowed_roles:
                return view_func(request, *args, **kwargs)
            else:
                messages.error(request, 'You are not authorized') 
                return redirect('index')
            return view_func(request, *args, **kwargs)
        return wrapper_func
    return decorator