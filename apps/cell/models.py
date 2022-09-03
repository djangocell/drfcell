from django.db import models


class Cell(models.Model):
    name = models.CharField(max_length=100, primary_key=True)
    damage = models.IntegerField(default=0)
    upgrade_resource = models.IntegerField(default=0)


class Upgrade(models.Model):
    current = models.ForeignKey(Cell, on_delete=models.CASCADE, related_name="current_cell")
    # comment = models.CharField(max_length=100)
    next = models.ForeignKey(Cell, on_delete=models.CASCADE, blank=True, related_name="next_cell")
