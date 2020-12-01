
from django.urls import path
from bankapi import views

urlpatterns = [ 
    path('datacreate/', views.bankloneApi.as_view()),
    path('datacreate/<int:pk>/', views.bankloneApi.as_view()),
]
