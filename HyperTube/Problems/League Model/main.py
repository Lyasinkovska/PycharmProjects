from django.db import models
from django.db.models import CharField, ForeignKey, IntegerField


class Team(models.Model):
    name = models.CharField(max_length=64)

    class Meta:
        app_label = 'tournament'


class League(models.Model):

    class Meta:
        app_label = 'tournament'