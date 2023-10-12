from django.urls import path

from .views import index, auth, signup

urlpatterns = [
    path('', index),
    path('auth/', auth),
    path('signup/', signup)
]
