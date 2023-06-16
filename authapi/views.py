from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import UserSerializer
from .models import User
from rest_framework.response import Response
from django.contrib.auth import authenticate, login
from django.views.decorators.csrf import csrf_exempt
# from .api_function import *
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from .auth_function import *
# from rest_framework_simplejwt.tokens import RefreshToken

# Create your views here.
class UserView(APIView):
    def get(self,request,user_data):
        user = UserService.get_data(user_data)
        if user:
            serializer = UserSerializer(user)
            return Response(serializer.data,status=200)
        
    def put(self, request, user_data):
        user = UserService.get_data(user_data)
        try:
            serializer = UserSerializer(user, data=request.data)
            if serializer.is_valid():
                serializer.save()
                updated_user = UserService.update_user(user, request.data)
                return Response(UserSerializer(updated_user).data, status=200)
            return Response(serializer.errors, status=400)
        except:
            return Response({"message": "User not found"}, status=400)
        
class LoginView(APIView):
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        role=request.data.get('role')
        if email is None or password is None or role is None:
            return Response({'error': 'Please provide email, password, and role.'}, status=400)

        user = authenticate(request, email=email, password=password,role=role)

        if user is None:
            return Response({'error': 'Invalid email or password.'}, status=401)

        if user.role != role:
            return Response({'error': 'Invalid role.'}, status=401)

        login(request, user)
        return Response({'message': 'Login successful.'}, status=200)  
            

class CreateView(APIView):
    def post(self, request):
        seralizer=UserSerializer(data=request.data)
        if seralizer.is_valid():
            user_data=seralizer.validated_data
            user = UserService.create_user(user_data)
            print(user)
            return Response(UserSerializer(user).data, status=201)
        return Response(seralizer.errors, status=400)
        
       
