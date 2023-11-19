# myapp/context_processors.py
from django.contrib.auth import get_user_model
from .models import Members

def user_details(request):
    
    user = ""
    photo = ""
    fullname = ""
    role = ""
    mobile = request.session.get('mobile')
    if mobile:
        user = Members.objects.get(mobile=mobile)
        if user:
            photo = user.photo
            fullname = user.fullname
            mobile = user.mobile
            photo =user.photo
            role = user.role
            if not photo:
                photo = "noimage.png"

    user = {
                    'fullname' : fullname,
                    'mobile' : mobile,
                    'photo' : photo,
                    'role' : role,
                    'appname' : 'Event App',
         }
    return {'userdetails': user}
