from django.db import models
from users.models import User
from adminsite.validators import validate_phone_number


class BaseUser(User):
    
    name = models.CharField(max_length=128)
    photo = models.ImageField(upload_to='albums/userphoto/%Y/%m/%d', blank=True, null=True)
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

    def save(self, *args, **kwargs):
        self.full_clean()
        self.set_password(self.password)
        super(BaseUser, self).save(*args, **kwargs)



class AdminUser(BaseUser):
    phone = models.CharField(max_length=13, validators=[validate_phone_number])

    def save(self, *args, **kwargs):
        self.full_clean()
        self.type = "admin"
        self.is_staff = True
        super(AdminUser, self).save(*args, **kwargs)
