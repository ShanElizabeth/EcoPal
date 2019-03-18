from django.shortcuts import render
from . import views
from search.models import Saved_search

def getFavSearch(request):
	obj=Saved_search.objects.get()
	context={
	"object":obj
	}
	return render(request,"profile.html",context)

#    i = 9
#    context = {}
#    while i <= Saved_search.objects.count():
#        c = Saved_search.objects.get(id=i)
#        context["object" + str(i)] = c
#        i+=1
#        print(c)