# Generated by Django 4.2.5 on 2023-10-12 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('time', models.TimeField(db_index=True)),
                ('data', models.DateField(db_index=True)),
                ('day_of_week', models.CharField(max_length=30, null=True)),
                ('teacher_id', models.IntegerField(null=True)),
            ],
        ),
    ]
