from django.contrib import admin
from .models import userInputChatbot #to see our database
from .models import saveAnswer

# Register your models here.
admin.site.register(userInputChatbot)
admin.site.register(saveAnswer)