from django.db import models


class Cell(models.Model):
    name = models.CharField(max_length=100)
    damage = models.IntegerField(default=0)
    next_cell = models.ManyToManyField("self")
    upgrade_resource = models.IntegerField(default=0)
