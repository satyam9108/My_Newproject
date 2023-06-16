from .views import *
from django.urls import path,include
urlpatterns = [
    path('feedback/', FeedbackView.as_view(), name='feedback'), 
    path('feedback/<int:user_id>/', SpecificFeedback.as_view(), name='user'),


]