from django.contrib import admin
from .models import WorkerUser
from administrators.admin import BaseUserAdmin


@admin.register(WorkerUser)
class SalesmanAdmin(BaseUserAdmin):
    icon = '<i class="material-icons">accessibility</i>'
    search_fields = [
        'phone',
        'name',
        'email',
    ]
    list_filter = [
        'is_active',
    ]