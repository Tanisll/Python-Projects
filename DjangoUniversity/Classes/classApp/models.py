from django.db import models
from django.db.models import Model
from django.db.models import Manager


class djangoClasses(models.Model):
    title = models.CharField(max_length=50, default='', blank=False, null=False)
    courseNumber = models.IntegerField(max_length=10, default='', blank=False, null=False)
    instructorName = models.CharField(max_length=80, default='', blank=False, null=False)
    duration = models.FloatField(max_length=30, default='', blank=False, null=False)

    objects = models.Manager()


def __str__(self):
    return self.name
