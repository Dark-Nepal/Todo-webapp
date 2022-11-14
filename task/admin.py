from django.contrib import admin
from .models import Task

class TaskAdmin(admin.ModelAdmin):

    list_display = (
        'title',
        'description',
        'completed',
        'created',

    )

    fields = (
        'title',
        'description',
        'completed',
    )

    list_filter = ('created',)

admin.site.register(Task , TaskAdmin)