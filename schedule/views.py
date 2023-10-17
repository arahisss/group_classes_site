from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.http import HttpResponseNotFound
from django.shortcuts import render, redirect
from django.template import loader
from django.urls import reverse_lazy
from .forms import *
from .models import Lesson
from django.views.generic.edit import CreateView
from .forms import LessonForm
from django.contrib import messages
from .forms import LoginUserForm


# class LessonCreateView(CreateView):
#     template_name = 'schedule/create.html'
#     form_class = LessonForm
#     success_url = '/schedule/'
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context[]


def index(request):
    return render(request, "index.html")


def signup(request):
    return render(request, "register.html")


class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'register.html'
    success_url = reverse_lazy('schedule')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'login.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def get_success_url(self):
        return reverse_lazy('schedule')


@login_required
def schedule(request):
    lessons = Lesson.objects.all()
    return render(request, 'schedule.html', {'lessons': lessons})


def page_not_found(request, exception):
    return HttpResponseNotFound("<h1>Страница не найдена :(</h1>")
