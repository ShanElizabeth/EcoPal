from django.urls import path
from . import views
from django.views.generic.base import TemplateView
urlpatterns = [
    path('', TemplateView.as_view(template_name='chatbotold.html'),name="chatbot"),
    path('ask/', views.getResponse),
    path('saveanswer/',views.saveanswer),
    path('response/',views.display),
]