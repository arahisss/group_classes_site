from django.urls import path
from django.contrib import admin
from .views import *
from django. contrib.auth. views import PasswordResetView, PasswordResetConfirmView, PasswordResetDoneView

urlpatterns = [
    path('', index, name='home'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('register/', RegisterUser.as_view(), name='register'),

    path('password_reset/', PasswordResetView.as_view(
        template_name='reset_password.html',
        subject_template_name='reset_subject.txt',
        email_template_name='reset_email.txt'),
         name='password_reset'),

    path('password_reset/done/', PasswordResetDoneView.as_view(
        template_name='email_sent.html'), name='password_reset_done'),

    path('reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(
        template_name='confirm_password.html'),
         name='password_reset_confirm'),

    path('change_password/', ChangePassword.as_view(), name='change_password'),
    # path('change_password/', ChangePassword.as_view(), name='change_password'),

    path('schedule/', schedule, name='schedule'),
    path('add_lesson/', AddLesson.as_view(), name='add_lesson'),
    path('delete_lesson/', delete_lesson, name='delete_lesson'),

    path('my_schedule/', my_schedule, name='my_schedule'),
    path('add_user_lesson/', add_user_lesson, name='add_user_lesson')

]
