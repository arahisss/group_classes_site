from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

# будет таблица записей, где к id каждого юзера будет id занятия


# class Profile(models.Model):
#     user = models.OneToOneField(settings.AUTH_USER_MODEL)
#     role = models.IntegerField(null=True, max_length=2, verbose_name='Роль')
#


class Lesson(models.Model):
    title = models.CharField(max_length=50, null=True, verbose_name='Урок')
    description = models.TextField(null=True, blank=True, verbose_name='Описание')
    time = models.TimeField(db_index=True, verbose_name='Время')
    data = models.DateField(db_index=True, verbose_name='Дата')
    # teacher_id = models.IntegerField(null=True, verbose_name='id учителя')

    teacher_id = models.ForeignKey(User, null=True, on_delete=models.CASCADE, verbose_name='id учителя')

    class Meta:
        verbose_name_plural = 'Занятия'
        verbose_name = 'Занятие'
        ordering = ['-data']

