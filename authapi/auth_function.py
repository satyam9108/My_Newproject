from rest_framework.response import Response
from .models import User
from rest_framework.response import Response

class UserService:
    def get_data(user_data):
        try:
            user = User.objects.get(id=user_data)
            return user
        except User.DoesNotExist:
                 return None

    def update_user(user, user_data):
        user.email = user_data.get('email', user.email)
        user.password = user_data.get('password', user.password)
        user.role = user_data.get('role', user.role) 
        user.save()
        return user
    
    def create_user(data):  
        user = User(
            email=data.get('email'),
            password=data.get('password'),
            role=data.get('role')
        )
        user.save()
        return user 
    