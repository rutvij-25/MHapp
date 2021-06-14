from django.contrib.auth.models import User
from django.db.models.signals import post_save
from .models import UserModel
from django.dispatch import receiver

@receiver(post_save,sender=User)
def CreateUserModel(sender,instance,created,**kwargs):
    if created:
        UserModel.objects.create(user = instance)
    

