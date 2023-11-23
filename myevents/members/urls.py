from . import views
from django.urls import path, include


urlpatterns = [
   
    path('member_update/<str:mid>', views.member_update, name="member_update"),
    path('member_view', views.member_view, name="member_view"),
    path('member_delete/<str:mid>/', views.member_delete, name='member_delete'),
    path('member_edit', views.member_edit, name="member_edit"),
    path('member_edits/<str:compound>/', views.member_edits, name="member_edit"),
]

