from django.db import models
from django.utils import timezone

class Question (models.Model) : 

    question_title = models.CharField(max_length=300)
    description = models.TextField(blank=True, null=True)
    created_on = models.DateTimeField(default=timezone.now())

    def __str__(self) : 
        return self.question_title


class Choice (models.Model) : 

    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name="choices")
    choice = models.CharField(max_length=300)
    created_on = models.DateTimeField(default=timezone.now())

    #   returns the name of the choice
    def __str__(self) : 
        return self.choice


