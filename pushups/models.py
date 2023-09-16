import jsonfield as jsonfield
from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User


class BenchmarkTest(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    pushups = models.IntegerField()
    date = models.DateField(default=timezone.now())


class WorkoutType(models.Model):
    benchmark = models.IntegerField()
    difficulty = models.IntegerField()
    week = models.IntegerField()
    day = models.IntegerField()
    sets = jsonfield.JSONField(default=[])


class Workout(models.Model):
    type = models.ForeignKey(WorkoutType, null=True, on_delete=models.SET_NULL)
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    date = models.DateField(default=timezone.now())
    sets_completed = jsonfield.JSONField(default=[])
    total_pushups = models.IntegerField(default=0)
