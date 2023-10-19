from django.contrib import admin

from .models import Lesson, LessonUser


class ScheduleAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'time', 'data', 'teacher_id')
    list_display_links = ('title', 'data')
    search_fields = ('title', 'data', )


class LessonUserAdmin(admin.ModelAdmin):
    list_display = ('user', 'lesson')
    list_display_links = ('user', 'lesson')
    search_fields = ('user', 'lesson')


admin.site.register(Lesson, ScheduleAdmin)
admin.site.register(LessonUser, LessonUserAdmin)
