from rest_framework import serializers
from .models import * 

class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = ['id','user', 'name','title','rating','message',]