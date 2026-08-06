from django.db import models

from .harvest import Harvest


class HarvestQuality(models.Model):

    QUALITY = (
        ("special", "درجه ممتاز"),
        ("grade1", "درجه یک"),
        ("grade2", "درجه دو"),
        ("grade3", "درجه سه"),
        ("waste", "ضایعات"),
    )

    harvest = models.ForeignKey(
        Harvest,
        on_delete=models.CASCADE,
        related_name="qualities"
    )

    quality = models.CharField(
        max_length=20,
        choices=QUALITY
    )

    weight = models.DecimalField(
        max_digits=12,
        decimal_places=2
    )

    description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.harvest.code}-{self.quality}"