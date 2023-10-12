from django.contrib import admin

from .models import Lesson


class ScheduleAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'time', 'data', 'day_of_week', 'teacher_id')
    list_display_links = ('title', 'data', 'day_of_week')
    search_fields = ('title', 'data', )


admin.site.register(Lesson, ScheduleAdmin)
