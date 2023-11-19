from django.shortcuts import render, HttpResponse, redirect
from .models import Members
from django.contrib import messages
import logging
from .login_required import my_login_required
from datetime import datetime




def index(request):
    return redirect('dashboard')


def login(request):
    mobile = ""
    password = ""
    lastlogin = datetime.now()

    if request.method == "POST":
        mobile = request.POST.get("username")
        password = request.POST.get("password")

        if mobile and password:
            Usercheck = Members.objects.filter(mobile=mobile).exists()
            if Usercheck:
                user = Members.objects.get(mobile=mobile)
                user.lastlogin = lastlogin
                user.save()
                if user.password == password:
                    request.session["mobile"] = mobile
                    return redirect('dashboard')
                else:
                    messages.error(request, "Sorry, Incorrect Password")
                    logging.error('Error message')


            else:
                messages.error(request, "Sorry, Mobile No. does not exists")
    context = {'mobile' : mobile, }
    return render(request, 'login.html' , context)

@my_login_required
def dashboard(request):
   name = ""
   name = request.GET.get('name') if request.GET.get('name') else ""
       
    
   context = {
        'name' : name

   }
   return render(request, 'dashboard.html', context)
# Create your views here.

def logout(req):
      req.session.clear()
      return redirect('login')


