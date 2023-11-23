from django.db import models
import uuid


class Members(models.Model):
    fullname = models.CharField(max_length=50)
    mobile = models.CharField(max_length=50, unique=True)
    role = models.CharField(max_length=50,null=True, blank=True)
    status = models.CharField(max_length=50,null=True, blank=True)
    lastlogin = models.DateTimeField(auto_now=False, auto_now_add=False,null=True, blank=True)
    photo = models.CharField(max_length=100,null=True, blank=True)
    password = models.CharField(max_length=50, default="123456")
    id = models.IntegerField(primary_key=True,  editable=False)
    mid = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)


class Events(models.Model):
    eventname = models.CharField(max_length=50)
    eid = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)
    description = models.TextField(blank=True, null=True)


class EventDetails(models.Model):
    eventname = models.CharField(max_length=50)
    eid = models.UUIDField(editable=False)
    startdate = models.DateField()
    enddate = models.DateField()
    status = models.CharField(max_length=50)
    addeddate = models.DateField(auto_now=True)
    addedtime = models.TimeField(auto_now=True)
    payments = models.IntegerField(blank=True, null=True)
    purchase = models.IntegerField(blank=True, null=True)
    members = models.IntegerField(blank=True, null=True)


