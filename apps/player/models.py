from django.db import models


class Status(models.Model):
    user = models.CharField(max_length=100)
    resource = models.IntegerField(default=0)
