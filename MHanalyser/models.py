from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class UserModel(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    answers = models.TextField(null=True)
    result = models.IntegerField(null=True)

    def __str__(self):
        return str(self.user)


