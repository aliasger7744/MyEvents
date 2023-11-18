from django.db import models

class Members(models.Model):
    fullname = models.CharField(max_length=50)
    mobile = models.CharField(max_length=50, unique=True)
    role = models.CharField(max_length=50,null=True, blank=True)
    lastlogin = models.DateTimeField(auto_now=False, auto_now_add=False,null=True, blank=True)
    photo = models.CharField(max_length=100,null=True, blank=True)
    password = models.CharField(max_length=50, default="123456")
