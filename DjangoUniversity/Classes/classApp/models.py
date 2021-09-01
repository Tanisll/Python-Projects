from django.db import models
from models import djangoClasses
from django.db.models import Model
from django.db.models import Manager


class djangoClasses(models.Model):
    title = models.CharField(max_length=50, default='', blank=False, null=False)
    courseNumber = models.IntegerField(max_length=10, default='', blank=False, null=False)
    instructorName = models.CharField(max_length=80, default='', blank=False, null=False)
    duration = models.FloatField(max_length=30, default='', blank=False, null=False)

    class1 = djangoClasses(title="Math", courseNumber=13, instructorName="Jerry White", duration= 15.25)
    class2 = djangoClasses(title="Literature", courseNumber=9, instructorName="Scott Housing", duration= 20.5)
    class3 = djangoClasses(title="Art II", courseNumber=18, instructorName="Phil Murphy", duration= 12.5)

    class1.save()
    class2.save()
    class3.save()

def __str__(self):
    return self.name
