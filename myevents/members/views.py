from django.shortcuts import render,HttpResponse,get_object_or_404, redirect
from django.core.files.storage import default_storage
from myapp.models import Members
from django.contrib import messages
from django.urls import reverse
import os
import uuid

def member_update(req, mid):
      
      fullname = ""
      password = ""
      mobile = ""
      photo = ""
      role = ""


      if mid == '0' :
            mid = None
            buttontitle= "+ Add"
      else:
            mid = mid
            buttontitle = "Update"
      if not mid:
             mtitle = "Add New Member"
      if mid:
             try:
                userd = Members.objects.filter(mid=mid).exists()
                if not userd:
                      messages.error(req, 'Opps, Member not exists')
                      return redirect('member:member_view')
                else:
                      userd = Members.objects.get(mid=mid)
                      mobile = userd.mobile
                      fullname = userd.fullname
                      password = userd.password
                      role = userd.role
                      photo = userd.photo
                      mtitle = f"Edit: {fullname} [{mobile}]"
             except Exception as e:
                   messages.error(req, 'Opps, Member not exists')
                   return redirect('member:member_view')
                   



      

      if req.method == "POST":
        fullname = req.POST.get('fullname')  
        mobile = req.POST.get('mobile')
        photo = req.FILES.get('photo')
        role = req.POST.get('role')
        password = req.POST.get('password')
        mid = req.POST.get('mid')
        mid = "" if mid == "None" or mid is None or mid == "0" else mid
        #formdate = f"{fullname},{mobile},{photo},{role},{password}"
        #return HttpResponse(formdate)
        #return HttpResponse(photo_file)
        if photo:
              # Save the photo to the media directory
              unique_filename = str(uuid.uuid4()) + os.path.splitext(photo.name)[1]
              unique_filename = f"{ os.path.splitext(photo.name)[0]}_{unique_filename}"
              file_path = os.path.join('static/images', unique_filename)
              
              #return HttpResponse(file_path)
              with default_storage.open(file_path, 'wb') as destination:
                  for chunk in photo.chunks():
                      destination.write(chunk)

              image_url = unique_filename

        #return HttpResponse(mid)   
        if mid and mid is not None:
            try:
                userd = Members.objects.get(mid=mid)
                if not userd:
                      messages.error(req, 'Opps, Member not exists')
                      return redirect('member:member_view')
                else:
                      userd = Members.objects.get(mid=mid)
                      userd.mobile = mobile
                      userd.fullname = fullname
                      userd.password = password
                      userd.role = role
                      if photo:
                        userd.photo = image_url
                      userd.save()
                      messages.success(req, 'Member updated successfully')
                      return redirect('member:member_view')
            except Exception as e:
                   messages.error(req, 'Opps, Member not exists')
                   return redirect('member:member_view')
        else:
          if mobile:
                users = Members.objects.filter(mobile=mobile).exists()
                if users:
                      messages.error(req, 'Mobile no. already exists')   
                else:
                      usersadd = Members(fullname=fullname,mobile=mobile,role=role,photo=image_url,password=password)  
                      usersadd.save()
                      messages.success(req,'Member added successfully')
                      return redirect('member:member_view')

      context = {
                  'mtitle' : mtitle,
                  'buttontitle' : buttontitle,
                  'mid' : mid,
                  'fullname' :  fullname,
                  'password' : password,
                  'mobile' : mobile,
                  'photo' : photo,
                  'role' : role
                }
      return render(req, "member_update.html", context)

def member_view(req):
       data = Members.objects.all()
       total_members = Members.objects.count()

       context = {
                'data' : data,
                'mcount' : total_members
                }
       
       return render(req, "member_view.html", context)


def member_delete(req,mid):
       if mid:
              adminmember = Members.objects.get(mid=mid)
              if adminmember.mobile == "7045277352":
                     messages.error(req,"Member deletetion failed")
                     return redirect('member:member_view')
              
              Members.objects.filter(mid=mid).delete()
              messages.success(req,"Member deleted successfully")
       return redirect('member:member_view')


def member_edit(req):
       return HttpResponse("member_edit")
