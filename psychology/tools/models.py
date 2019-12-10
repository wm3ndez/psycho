from django.db import models


class Activity(models.Model):
    activity = models.CharField(max_length=100)
    day = models.DateField(max_length=100)
    started_at = models.TimeField(max_length=100)
    ended_at = models.TimeField(max_length=100)
    expectation = models.PositiveSmallIntegerField()
    pleasure = models.PositiveSmallIntegerField()
    achievement = models.PositiveSmallIntegerField()

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
