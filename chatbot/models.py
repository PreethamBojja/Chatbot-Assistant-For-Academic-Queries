from django.db import models


# Create your models here.

class registration(models.Model):
    branch = models.CharField(max_length=3)
    venue = models.CharField(max_length=20)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    def __str__(self):
        return self.branch
