from django.db import models
from .survey import Survey


class QuestionManager(models.Manager):
    pass


class Question(models.Model):
    types = (
        ('txt', 'Text answer'),
        ('num', 'Choose one answer'),
        ('nums', 'Choose many answers'),
    )

    text = models.TextField(blank=True)
    type = models.CharField(max_length=4, choices=types)
    num = models.PositiveIntegerField()

    survey = models.ForeignKey(Survey, on_delete=models.PROTECT)

    objects = QuestionManager()
