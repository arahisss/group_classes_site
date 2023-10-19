from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.forms import ModelForm

from .models import *


class LessonForm(ModelForm):
    title = forms.CharField(label='Урок', widget=forms.TextInput(attrs={'class': 'form-control', 'style': 'width: 300px;'}))
    description = forms.CharField(label='Описание', widget=forms.Textarea(attrs={'class': 'form-control', 'style': 'width: 300px;', 'rows': 5}))
    time = forms.CharField(label='Время', widget=forms.TextInput(attrs={'class': 'form-control', 'style': 'width: 300px;'}))
    data = forms.DateField(label='Дата', widget=forms.TextInput(attrs={'class': 'form-control', 'style': 'width: 300px;'}))

    class Meta:
        model = Lesson
        fields = ('title', 'description', 'time', 'data')


class LessonUserForm(ModelForm):
    lesson = forms.CharField(label='Урок', widget=forms.TextInput(attrs={'class': 'form-control', 'style': 'width: 300px;', 'data-lesson': ''}))

    class Meta:
        model = LessonUser
        fields = ('user', 'lesson',)


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Имя пользователя', widget=forms.TextInput(attrs={'class': 'form-control', 'style': 'width: 300px;'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-control', 'style': 'width: 300px;'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password')


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-control', 'style': 'width: 300px;'}))
    email = forms.CharField(label='Email', widget=forms.TextInput(attrs={'class': 'form-control', 'style': 'width: 300px;'}))
    first_name = forms.CharField(label='Имя', widget=forms.TextInput(attrs={'class': 'form-control', 'style': 'width: 300px;'}))
    last_name = forms.CharField(label='Фамилия', widget=forms.TextInput(attrs={'class': 'form-control', 'style': 'width: 300px;'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-control', 'style': 'width: 300px;'}))
    password2 = forms.CharField(label='Повтор пароля', widget=forms.PasswordInput(attrs={'class': 'form-control', 'style': 'width: 300px;'}))
    groups = forms.RadioSelect()

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'groups', 'last_name', 'password1', 'password2')

