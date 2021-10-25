from django.db import models
from django.contrib.auth.models import User

from .survey import Survey

class AccountManager(models.Manager):
    pass


class Account(models.Model):
    id = models.UUIDField(editable=False, primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    survey = models.ManyToManyField(Survey)

    objects = AccountManager()

