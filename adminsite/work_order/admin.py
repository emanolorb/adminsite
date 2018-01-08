from django.contrib import admin
from .models import WorkOrder

# Register your models here.

@admin.register(WorkOrder)
class WorkOrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'opening_date', 'number', 'customer', 'description', 'is_active']
    fields = ['opening_date', 'number', 'customer', 'description', 'is_active']