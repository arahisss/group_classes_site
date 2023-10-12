from django.urls import path

from .views import index, auth, signup, schedule

urlpatterns = [
    path('', index),
    path('auth/', auth),
    path('signup/', signup),
    path('schedule/', schedule)
]
