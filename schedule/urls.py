from django.urls import path
from django.contrib import admin
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('schedule/', schedule, name='schedule'),
    path('add_lesson/', AddLesson.as_view(), name='add_lesson'),

]
