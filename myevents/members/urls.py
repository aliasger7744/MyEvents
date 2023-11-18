from . import views
from django.urls import path, include

urlpatterns = [
   
    path('member_update', views.member_update, name="member_update"),
    path('member_view', views.member_view, name="member_view"),
    path('member_delete', views.member_delete, name="member_delete"),
    path('member_edit', views.member_edit, name="member_edit"),
]