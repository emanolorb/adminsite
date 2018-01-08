from django.db import models
from adminsite.validators import validate_phone_number
from enumfields import EnumIntegerField
from .enums import Rating


class Customer(models.Model):
    name = models.CharField(max_length=80)
    phone = models.CharField(max_length=13, validators=[validate_phone_number], null=True, blank=True)
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
