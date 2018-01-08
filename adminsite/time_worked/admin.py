from django.contrib import admin
from .models import TimeWorked


# Register your models here.
@admin.register(TimeWorked)
class TimeWorkedAdmin(admin.ModelAdmin):
    list_display = ['user_id','user', 'date', 'start', 'finish', 'context', 'work_order']
    fields = ['user', 'date', 'start', 'finish', 'context', 'work_order', 'img']
    search_fields = [
        'date',
    ]
    # list_filter = [
    #     'is_active',
    # ]
