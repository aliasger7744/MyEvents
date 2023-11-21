from django.shortcuts import render, HttpResponse

# Create your views here.

def event_view(req):
     return HttpResponse("ok")


def event_update(req, eid):
     return HttpResponse(eid)


def event_delete(req,eid):
     return HttpResponse(eid)

def event_edit(req,eid):
     return HttpResponse(eid)
    
