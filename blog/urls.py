# blog/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='blog_index'),
    # Add more patterns for specific blog views as needed
]
