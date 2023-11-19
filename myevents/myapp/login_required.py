from functools import wraps
from django.shortcuts import redirect
from django.urls import reverse

def my_login_required(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        if not 'mobile' in request.session:
            # Redirect to the login page
            return redirect(reverse('login'))  # Replace 'custom_login' with your login URL
        return view_func(request, *args, **kwargs)
    return _wrapped_view
