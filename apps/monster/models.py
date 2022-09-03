from django.db import models


class Monster(models.Model):
    name = models.CharField(max_length=100)
    resource = models.IntegerField(default=0)
