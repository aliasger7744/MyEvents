# myapp/context_processors.py
from django.contrib.auth import get_user_model

def user_details(request):
    
    user = {
            'fullname' : 'ALiasger',
            'mobile' : request.session.get("mobile", False)
           }
    return {'user': user}
