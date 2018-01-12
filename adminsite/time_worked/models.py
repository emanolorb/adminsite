from django.db import models
from users.models import User
from work_order.models import WorkOrder

# Create your models here.
class TimeWorked(models.Model):
    # Datos generales
    user = models.ForeignKey(User)
    date = models.CharField(max_length=80, blank=True)
    start = models.CharField(max_length=80, blank=True)
    finish = models.CharField(max_length=20, blank=True)
    context = models.CharField(max_length=120, blank=True)
    work_order = models.ForeignKey(WorkOrder)
    location = models.CharField(max_length=120, blank=True)
    img = models.ImageField(upload_to='albums/images/%Y/%m/%d')
    hours = models.IntegerField()
    minutes = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True, editable=False)

    def __str__(self):
        return "%s - %s" % (self.user.id, self.date)
