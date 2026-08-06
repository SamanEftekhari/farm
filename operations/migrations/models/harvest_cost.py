from django.db import models

from .harvest import Harvest


class HarvestCost(models.Model):

    harvest = models.ForeignKey(
        Harvest,
        on_delete=models.CASCADE,
        related_name="costs"
    )

    title = models.CharField(
        max_length=200
    )

    amount = models.DecimalField(
        max_digits=12,
        decimal_places=2
    )

    description = models.TextField(blank=True)

    def __str__(self):
        return self.title