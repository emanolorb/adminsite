from django.contrib import admin
from .models import TimeWorked


# Register your models here.
@admin.register(TimeWorked)
class TimeWorkedAdmin(admin.ModelAdmin):
    list_display = ['user_id','user', 'date', 'start', 'finish', 'context', 'work_order', 'hours', 'minutes']
    # fields = ['user', 'date', 'start', 'finish', 'context', 'work_order', 'img']
    search_fields = [
        'context',
    ]
    list_filter = (
        'user',
        'date',
        )
    fieldsets = (
        ('User', {
            'fields': (
                    'user',
                )
        }),
        ('Work', {
            'fields': (
                'date',
                'start',
                'finish',
                'context',
                'img',
            )
        }),
        ('Work Order', {
            'fields': (
                'work_order',
            )
        }),
    )