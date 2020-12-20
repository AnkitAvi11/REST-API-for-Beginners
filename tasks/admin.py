from django.contrib import admin

from .models import Task

class TaskAdmin(admin.ModelAdmin) : 
    list_display = ('id', 'user', 'title', 'completion_date', 'status')
    list_display_links = ('id', 'user', 'title')
    list_editable = ('status',)

admin.site.register(Task, TaskAdmin)