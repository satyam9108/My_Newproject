from django.db import models
from django.conf import settings
# Create your models here.
class Feedback(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,blank=True,null=True)
    name=models.CharField(max_length=40,blank=True,null=True)
    title=models.CharField(max_length=50,blank=True,null=True)
    rating=models.FloatField(blank=True,null=True)
    message = models.TextField(blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True,blank=True,null=True)

    def __str__(self):
        return self.name
    
    # just comment