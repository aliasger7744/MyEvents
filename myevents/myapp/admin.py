from django.contrib import admin
from .models import Members, Events, EventDetails

admin.site.register(Members)
admin.site.register(Events)
admin.site.register(EventDetails)

# Register your models here.
