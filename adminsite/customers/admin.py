from django.contrib import admin
from .models import Customer, CustomerRating

# Register your models here.
@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'phone', 'email', 'cr', 'is_active', 'created_at']
    fields = ['name', 'phone', 'email', 'cr', 'is_active']
    search_fields = [
        'name',
        'phone',
    ]
    readonly_fields = [
        'email',
    ]


@admin.register(CustomerRating)
class CustomerRatingAdmin(admin.ModelAdmin):
    list_display = ['id', 'customer', 'rating', 'description']
    
