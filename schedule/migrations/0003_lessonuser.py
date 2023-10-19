# Generated by Django 4.2.5 on 2023-10-18 21:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('schedule', '0002_alter_lesson_options_alter_lesson_data_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='LessonUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lesson', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='schedule.lesson', verbose_name='Занятие')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Пользователь-Занятие',
                'verbose_name_plural': 'Пользователи-Занятия',
            },
        ),
    ]
