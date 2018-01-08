from django.db import models
from customers.models import Customer


class WorkOrder(models.Model):
    opening_date = models.DateField()
    number = models.IntegerField()
    customer = models.ForeignKey(Customer)
    description = models.TextField(null=True, blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self, *args, **kwargs):
        return "%s - %s" % (self.number, self.opening_date)
