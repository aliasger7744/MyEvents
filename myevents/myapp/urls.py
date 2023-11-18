from . import views
from django.urls import path, include

urlpatterns = [
    
    path('', views.index, name="index"),
    path('login', views.login, name="login"),
    path('dashboard', views.dashboard, name="dashboard"),
    path('logout', views.logout, name="logout"),
 
]