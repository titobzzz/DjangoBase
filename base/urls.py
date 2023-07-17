from django.contrib import admin
from django.urls import path
from . import views 
  
urlpatterns =[
    path('registerPage/', views.registerPage, name="registerPage"),
    path('loginPage/', views.loginPage, name="loginPage"),
    path('userProfile/<str:pk>', views.userProfile, name='userProfile'),
    path('logOut/', views.logOut, name="logOut"),
    path('', views.home, name="home"),
    path('room/<str:pk>', views.room, name="room"),
    path('createRoom/', views.createRoom, name="createRoom"),
    path('deleteRoom/<str:pk>', views.deleteRoom, name="deleteRoom"),
    path('deleteMessage/<str:pk>', views.deleteMessage, name="deleteMessage"),
    path('updateRoom/<str:pk>', views.updateRoom, name="updateRoom"),
  ]