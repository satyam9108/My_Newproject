from .models import *



class FeedbackService:
    def create_feedback(data):  
            user = Feedback(
            user=data.get('user'),
            name=data.get('name'),
            title=data.get('title'),
            rating=data.get('rating'),
            message=data.get('message'),
            created_at=data.get('created_at')
            )
            user.save()
            return user 
    
    def get_feedback(id):
          user = Feedback.objects.get(id=id)
          return user