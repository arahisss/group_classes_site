# Generated by Django 4.2.5 on 2023-10-18 17:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('schedule', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='lesson',
            options={'ordering': ['-data'], 'verbose_name': 'Занятие', 'verbose_name_plural': 'Занятия'},
        ),
        migrations.AlterField(
            model_name='lesson',
            name='data',
            field=models.DateField(db_index=True, verbose_name='Дата'),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='teacher_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='id учителя'),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='time',
            field=models.TimeField(db_index=True, verbose_name='Время'),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='title',
            field=models.CharField(max_length=50, null=True, verbose_name='Урок'),
        ),
    ]
