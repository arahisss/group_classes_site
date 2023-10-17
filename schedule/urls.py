from django.urls import path
from django.contrib import admin
from .views import index, schedule, RegisterUser, LoginUser

urlpatterns = [
    path('', index, name='home'),
    path('login/', LoginUser.as_view(), name='login'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('schedule/', schedule, name='schedule')
]
