from django.urls import path
from . import views
from django.views.generic.base import TemplateView
urlpatterns=[
path('',views.displaypage),
path('get_response/',views.get_response),
]