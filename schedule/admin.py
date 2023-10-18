from django.contrib import admin

from .models import Lesson


class ScheduleAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'time', 'data', 'teacher_id')
    list_display_links = ('title', 'data')
    search_fields = ('title', 'data', )


admin.site.register(Lesson, ScheduleAdmin)
