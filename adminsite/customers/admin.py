from django.contrib import admin
from .models import Customer, CustomerRating, Commerce

# Register your models here.
@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['id', 'commerce', 'name', 'phone', 'email', 'cr', 'customer_since', 'is_active', 'created_at']
    # fields = ['commerce','name', 'phone', 'email', 'cr', 'customer_since', 'is_active']
    search_fields = [
        'name',
        'phone',
        'email',
    ]
    list_filter = (
        'is_active',
        'commerce',
        )
    fieldsets = (
        ('Commerce', {
            'fields': (
                    'commerce',
                )
        }),
        ('Afiliation', {
            'fields': (
                'name',
                'address',
                'phone',
                'email',
                'cr',
            )
        }),
        ('Status', {
            'fields': (
                'customer_since',
                'is_active',
            )
        }),
    )

@admin.register(CustomerRating)
class CustomerRatingAdmin(admin.ModelAdmin):
    list_display = ['id', 'customer', 'rating', 'description']
    
@admin.register(Commerce)
class CommerceAdmin(admin.ModelAdmin):
    list_display = ['id', 'commerce',]
    fields = ['commerce',]
    search_fields = [
        'id',
        'commerce',
    ]