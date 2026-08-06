from django.db import models

from .planting import Planting


class Harvest(models.Model):

    STATUS = (
        ("draft", "پیش نویس"),
        ("confirmed", "تایید شده"),
        ("closed", "بسته شده"),
    )

    code = models.CharField(
        max_length=30,
        unique=True
    )

    planting = models.ForeignKey(
        Planting,
        on_delete=models.PROTECT,
        related_name="harvests"
    )

    harvest_date = models.DateField()

    total_weight = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        default=0
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS,
        default="draft"
    )

    notes = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-harvest_date"]

    def __str__(self):
        return self.code