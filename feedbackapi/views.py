from django.shortcuts import render
from .serializer import FeedbackSerializer
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .feedback_fun import FeedbackService
from .models import *
# Create your views here.

class FeedbackView(APIView):
    def get(self, request, format=None):
        feedback = Feedback.objects.all()
        serializer = FeedbackSerializer(feedback, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = FeedbackSerializer(data=request.data)
        if serializer.is_valid():
            user_data = serializer.validated_data
            user = FeedbackService.create_feedback(user_data)
            return Response(FeedbackSerializer(user).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class SpecificFeedback(APIView):
    def get(self,request,user_id):
        feedback = FeedbackService.get_feedback(user_id)
        # print(user)
        if feedback:
            serializer = FeedbackSerializer(feedback)
            return Response(serializer.data,status=200)
    
    
   
    
