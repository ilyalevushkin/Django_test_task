from django.db import models
from .question import Question
from .account import Account

class AnswerManager(models.Manager):
    pass


class Answer(models.Model):
    text = models.TextField(blank=False)
    account = models.ForeignKey(Account, on_delete=models.PROTECT)
    question = models.ForeignKey(Question, on_delete=models.PROTECT)

    objects = AnswerManager()
