from django.http import HttpResponseForbidden
from functools import wraps

def teacher_required(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        # Check if the user is logged in and is a teacher
        if request.user.is_authenticated and request.user.role == "teacher":
            return view_func(request, *args, **kwargs)
        else:
            # If the user is not a teacher, return a forbidden response
            return HttpResponseForbidden("Access Forbidden")

    return _wrapped_view

def student_required(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        # Check if the user is logged in and is a teacher
        if request.user.is_authenticated and request.user.role == "student":
            return view_func(request, *args, **kwargs)
        else:
            # If the user is not a teacher, return a forbidden response
            return HttpResponseForbidden("Access Forbidden")
    
    return _wrapped_view

from django.contrib.auth.decorators import user_passes_test

def async_login_required(view_func):
    @wraps(view_func)
    async def _wrapped_view(request, *args, **kwargs):
        if request.user.is_authenticated:
            return await view_func(request, *args, **kwargs)
        else:
            # Handle unauthorized access here (e.g., redirect to login page)
            return HttpResponseForbidden("Access Forbidden")
    return _wrapped_view