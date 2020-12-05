from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save


class Userprofile(models.Model) : 
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )
    

    def __str__(self) : 
        return self.user.username



def createUserprofile(sender, **kwargs) : 
    if kwargs['created'] : 
        Userprofile.objects.create(kwargs['instance'])


post_save.connect(createUserprofile, User)