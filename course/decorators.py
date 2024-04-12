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

def admin_required(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        # Check if the user is logged in and is a teacher
        if request.user.is_authenticated and request.user.role == "admin":
            return view_func(request, *args, **kwargs)
        else:
            # If the user is not a teacher, return a forbidden response
            return HttpResponseForbidden("Access Forbidden")
    
    return _wrapped_view
