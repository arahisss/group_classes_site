from django.db import models

# будет таблица записей, где к id каждого юзера будет id занятия


class Lesson(models.Model):
    title = models.CharField(max_length=50, null=True, verbose_name='Урок')
    description = models.TextField(null=True, blank=True, verbose_name='Описание')
    time = models.TimeField(db_index=True, verbose_name='Время')
    data = models.DateField(db_index=True, verbose_name='Дата')
    day_of_week = models.CharField(max_length=30, null=True, verbose_name='День недели')
    teacher_id = models.IntegerField(null=True, verbose_name='id учителя')

    # teacher_id = models.ForeignKey('User', null=True, on_delete=models.PROTECT, verbose_name='id учителя')

    class Meta:
        verbose_name_plural = 'Занятия'
        verbose_name = 'Занятие'
        ordering = ['-data']

