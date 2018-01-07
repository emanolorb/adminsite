from django.contrib import admin
from .models import AdminUser


class BaseUserAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'email', 'phone', 'is_active']
    fields = ['name', 'phone', 'email', 'password', 'is_active']


# Register your models here.
@admin.register(AdminUser)
class CustomerAdmin(BaseUserAdmin):
    search_fields = [
        'phone',
        'name',
        'email',
    ]
    list_filter = [
        'is_active',
    ]