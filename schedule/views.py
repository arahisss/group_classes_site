from django.contrib.auth import logout, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.http import HttpResponseNotFound, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.template import loader
from django.urls import reverse_lazy
from django.views import View

from .forms import *
from .models import Lesson, LessonUser
from django.views.generic.edit import CreateView
from .forms import LessonForm
from django.contrib import messages
from .forms import LoginUserForm
from datetime import datetime, timedelta
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse


class AddLesson(LoginRequiredMixin, CreateView):
    template_name = 'add_lesson.html'
    form_class = LessonForm
    success_url = reverse_lazy('schedule')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def form_valid(self, form):
        form.instance.teacher_id = self.request.user
        return super().form_valid(form)


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

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('schedule')


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'login.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def get_success_url(self):
        return reverse_lazy('schedule')


def logout_user(request):
    logout(request)
    return redirect('login')


def add_user_lesson(request):
    lesson = request.POST.get('lesson')
    user = request.user
    LessonUser.objects.create(lesson=get_object_or_404(Lesson, id=lesson), user=user)

    return redirect('my_schedule')


@login_required
def schedule(request):
    start_date = datetime.now().date()
    while start_date.weekday() != 0:
        start_date = start_date - timedelta(days=1)

    lessons = Lesson.objects.filter(data__gte=start_date).order_by('data', 'time')
    dates = set()

    for i in lessons:
        dates.add(i.data)

    weeks = []
    cur_week = []
    k = 0
    for i in sorted(dates):
        if k >= 5:
            weeks.append(cur_week)
            cur_week = []
            k = 0
        cur_week.append(i)
        k += 1

    weeks.append(cur_week)
    active = weeks[0]
    del weeks[0]

    return render(request, 'schedule.html', {'lessons': lessons, 'weeks': weeks,
                                             'active': active, 'dates': sorted(dates)})


@login_required
def my_schedule(request):
    start_date = datetime.now().date()
    while start_date.weekday() != 0:
        start_date = start_date - timedelta(days=1)

    user = request.user
    role = user.groups.all()[0].id
    lessons = []

    if role == 1:
        lessons_user = LessonUser.objects.filter(user=user)
        for item in lessons_user:
            lessons.append(item.lesson)
    elif role == 2:
        lessons = Lesson.objects.filter(data__gte=start_date, teacher_id=user).order_by('data', 'time')

    dates = set()

    for i in lessons:
        dates.add(i.data)

    weeks = []
    cur_week = []
    k = 0
    for i in sorted(dates):
        if k >= 5:
            weeks.append(cur_week)
            cur_week = []
            k = 0
        cur_week.append(i)
        k += 1

    weeks.append(cur_week)
    active = weeks[0]
    del weeks[0]

    return render(request, 'my_schedule.html', {'lessons': lessons, 'weeks': weeks,
                                             'active': active, 'dates': sorted(dates)})


def page_not_found(request, exception):
    return HttpResponseNotFound("<h1>Страница не найдена :(</h1>")
