"""
URL configuration for Khoj Sewa project.
"""
from django.urls import path, include

urlpatterns = [
    path('', include('main.urls')),
]
