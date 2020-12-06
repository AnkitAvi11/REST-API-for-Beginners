from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.db.models.signals import post_save


class Userprofile(models.Model) : 
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.CharField(max_length=300)
    profile_pic = models.ImageField(upload_to='profile/%Y/%m/' ,default='default.png')
    joined_on = models.DateTimeField(default=timezone.now())

    def __str__(self) : 
        return self.user.username


def createUserprofile(sender, **kwargs) : 
    if kwargs['created'] : 
        Userprofile.objects.create(user=kwargs['instance'])


post_save.connect(createUserprofile, User)
