from django.shortcuts import render
from . import views
from django.views.generic import TemplateView,ListView
from chatbot.models import saveAnswer
# Create your views here.

#def  profile(request):
#	return render(request,"profile.html")

#def get(request)
def getFav(request):
	obj=saveAnswer.objects.all()
	context={
	"object":obj
	}
	return render(request,"profile.html",context)

