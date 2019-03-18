"""MyEcoPal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.views.generic.base import TemplateView
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from search import urls
from chatbot import urls
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('accounts/', include('django.contrib.auth.urls')), #signup, login etc
    path('search/', include('search.urls')),
    path('chatbot/', include('chatbot.urls')),
    path('profile/', views.getFavSearch),
    path('profile/', TemplateView.as_view(template_name='profile.html'), name='profile'),
    path('base/', TemplateView.as_view(template_name='base2.html'), name='base'),
    path('accounts/login/search/', include('search.urls')),
    path('accounts/logout/search/', include('search.urls')),
]


if settings.DEBUG: #javascript, CSS 
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
