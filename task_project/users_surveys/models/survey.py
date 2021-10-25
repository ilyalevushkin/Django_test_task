from django.db import models
from datetime import datetime


class SurveyManager(models.Manager):
    pass


class Survey(models.Model):
    name = models.CharField(max_length=30, blank=False)
    date_start = models.DateTimeField(default=datetime.now, editable=False)
    date_finish = models.DateTimeField(blank=False)
    description = models.TextField(blank=True)

    objects = SurveyManager()
