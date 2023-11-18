from django.shortcuts import render,HttpResponse

def member_update(req):
     
      return HttpResponse("member_update")

def member_view(req):
       return HttpResponse("member_view")


def member_delete(req):
       return HttpResponse("member_delete")


def member_edit(req):
       return HttpResponse("member_edit")
