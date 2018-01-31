from django.db import models
from adminsite.validators import validate_phone_number
from enumfields import EnumIntegerField
from .enums import Rating


class Commerce(models.Model):
    commerce = models.CharField(max_length=80)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True, editable=True)

    def __str__(self, *args, **kwargs):
        return "%s" % (self.commerce)

class Customer(models.Model):
    commerce = models.ForeignKey(Commerce)
    name = models.CharField(max_length=80)
    phone = models.CharField(max_length=13, validators=[validate_phone_number], null=True, blank=True)
    address = models.CharField(max_length=160, null=True, blank=True)
    email = models.EmailField()
    cr = models.CharField(max_length=80, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    customer_since = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True, editable=True)

    def __str__(self, *args, **kwargs):
        return "%s - %s" % (self.id, self.name)

class CustomerRating(models.Model):
    customer = models.ForeignKey(Customer)
    rating = EnumIntegerField(Rating)
    description = models.TextField(null=True, blank=True)

    def __str__(self, *args, **kwargs):
        return "%s - %s" % (self.customer, self.rating)
