from django.contrib import admin
from django.urls import path
from . import views 
  
app_name = "base"
urlpatterns =[
    path('', views.home, name="home"),
    path('room/<str:pk>', views.room, name="room"),
    path('createroom/', views.createRoom , name="createRoom")
  ]