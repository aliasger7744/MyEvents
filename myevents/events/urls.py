from events.views import *


from django.urls import path, include


urlpatterns = [
   
    path('event_view', event_view, name="event_view"),
    path('event_update/<int:eid>', event_update, name="event_update"),
    path('event_delete/<int:eid>', event_delete, name="event_delete"),
    path('event_edit/<int:eid>', event_edit, name="event_edit"),
    
]