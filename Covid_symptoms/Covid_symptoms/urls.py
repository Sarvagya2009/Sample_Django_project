"""Covid_symptoms URL Configuration

urls.py in API houses all the the functions of the api that we create while urls.py of the main api framwork page houses the link to this urls
"""
from django.contrib import admin
from django.urls import path, include
from API import views

urlpatterns = [
    path('', include('API.urls')),
    path('admin/', admin.site.urls),
]
