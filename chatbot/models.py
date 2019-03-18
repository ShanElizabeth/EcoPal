from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

# Create your models here.
class userInputChatbot(models.Model):
	text=models.TextField(max_length=70, null=True)
	
class saveAnswer(models.Model):
	user=models.ForeignKey(User,on_delete=models.CASCADE)
	answer=models.CharField(max_length=150,null=True)