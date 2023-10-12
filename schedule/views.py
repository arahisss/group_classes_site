from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from .models import Lesson


def index(request):
    return render(request, "index.html")


def auth(request):
    return render(request, "auth.html")


def signup(request):
    return render(request, "signup.html")


def schedule(request):
    lessons = Lesson.objects.all()
    return render(request, 'schedule.html', {'lessons': lessons})
