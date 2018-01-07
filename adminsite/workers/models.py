from django.db import models
from users.models import User
from adminsite.validators import validate_phone_number
from administrators.models import BaseUser

class WorkerUser(BaseUser):
    phone = models.CharField(max_length=13, validators=[validate_phone_number])

    def save(self, *args, **kwargs):
        self.full_clean()
        self.type = "worker"
        super(WorkerUser, self).save(*args, **kwargs)

    class Meta(BaseUser.Meta):
        pass