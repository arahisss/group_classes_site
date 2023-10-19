from django.db import models
from django.contrib.auth.models import User


class Lesson(models.Model):
    title = models.CharField(max_length=50, null=True, verbose_name='Урок')
    description = models.TextField(null=True, blank=True, verbose_name='Описание')
    time = models.TimeField(db_index=True, verbose_name='Время')
    data = models.DateField(db_index=True, verbose_name='Дата')
    teacher_id = models.ForeignKey(User, null=True, on_delete=models.CASCADE, verbose_name='id учителя')

    class Meta:
        verbose_name_plural = 'Занятия'
        verbose_name = 'Занятие'
        ordering = ['-data']


class LessonUser(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE, verbose_name='Пользователь')
    lesson = models.ForeignKey(Lesson, null=True, on_delete=models.CASCADE, verbose_name='Занятие')

    class Meta:
        verbose_name_plural = 'Пользователи-Занятия'
        verbose_name = 'Пользователь-Занятие'

