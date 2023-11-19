# myapp/context_processors.py
from django.contrib.auth import get_user_model
from .models import Members

def user_details(request):
    mobile = request.session.get('mobile')
    user = ""
    if mobile:
        user = Members.objects.get(mobile=mobile)
        if user:
            photo = user.photo
            if not photo:
                photo = "noimage.png"
            user = {
                    'fullname' : user.fullname,
                    'mobile' : user.mobile,
                    'photo' : photo,
                    'role' : user.role
                }
    return {'userdetails': user}
