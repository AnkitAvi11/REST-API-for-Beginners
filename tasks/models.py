from django.db import models

from django.contrib.auth.models import User
from django.utils import timezone

class Task(models.Model) : 
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    title = models.CharField(max_length=300)

    description = models.TextField(blank=True, null=True)

    completion_date = models.DateField(default=timezone.now())

    status = models.BooleanField(default=False)

    posted_on = models.DateTimeField(default=timezone.now())


    #   str function for the class
    def __str__(self) : 
        return self.title
