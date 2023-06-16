from django.urls import path
from authapi.views import *
from .views import  UserView
# from rest_framework_simplejwt.views import (
#     TokenObtainPairView,
# )

urlpatterns = [
    path('users/<int:user_data>/', UserView.as_view(), name='user'),
    path('users/create/', CreateView.as_view(), name='create_user'), 
    path('users/login/', LoginView.as_view(), name='login'), 

]