from django.db import models


class DjangoClasses(models.Model):
    title = models.CharField(max_length=50, default='', blank=False, null=False)
    courseNumber = models.IntegerField(default='', blank=False, null=False)
    instructorName = models.CharField(max_length=80, default='', blank=False, null=False)
    duration = models.FloatField(max_length=30, default='', blank=False, null=False)

    # This will display the 'title' field for each row in the database as opposed to
    # 'DjangoClasses object (1)'. It will now display Math or Literature
    def __str__(self):
        return self.title
