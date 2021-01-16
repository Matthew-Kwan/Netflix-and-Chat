"""
This module will contain the endpoints for the api
"""
from django.conf.urls import include
from django.urls import path
from . import views

urlpatterns = [
  path('shows/<int:pk>/', views.ShowIdentifier.as_view()),
  path('shows/', views.ShowList.as_view()),
  path('messages/', views.MessageList.as_view()),
  path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]