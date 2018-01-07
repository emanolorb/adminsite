from django.db import models
from users.models import User

# Create your models here.
class TimeWorked(models.Model):
    # Datos generales
    user = models.ForeignKey(User)
    date = models.CharField(max_length=80, blank=True)
    start = models.CharField(max_length=80, blank=True)
    finish = models.CharField(max_length=20, blank=True)
    context = models.CharField(max_length=120, blank=True)
    # # adjuntos
    # document = models.FileField(upload_to='documents/%Y/%m/%d')
    # uploaded_at = models.DateTimeField(auto_now_add=True, editable=False)

    def __str__(self):
        return "%s - %s" % (self.user.id, self.date)