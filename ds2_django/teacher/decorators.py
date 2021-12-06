from django.http import HttpResponse
from django.shortcuts import redirect


# a decorator function is a function that takes an other function like an argument
# view function here is v


def unauthenticated_user(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('/')
        else:
            return view_func(request, *args, **kwargs)
    return wrapper_func
