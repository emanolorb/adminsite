from django.db import models
from users.models import User
from adminsite.validators import validate_phone_number


class BaseUser(User):
    
    name = models.CharField(max_length=128)
    type = models.CharField(max_length=30, blank=True)

    # def save(self, *args, **kwargs):
    #     if not self.password.startswith('**********'):
    #         self.set_password(self.password)
    #     else:
    #         self.password = User.objects.get(id=self.id).password
    #     self.is_staff = Trues
    #     user = super(BaseUser, self)
    #     user.save(*args, **kwargs)
    #     user.groups.clear()
    #     group = Group.objects.get(name=self.type)
    #     user.groups.add(group)

    def __str__(self, *args, **kwargs):
        return self.email

class AdminUser(BaseUser):
    phone = models.CharField(max_length=13, validators=[validate_phone_number])

    def save(self, *args, **kwargs):
        self.full_clean()
        self.type = "admin"
        super(AdminUser, self).save(*args, **kwargs)

    class Meta(BaseUser.Meta):
        pass
