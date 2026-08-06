from django.db import models

from machinery.models import Machine
from .planting import Planting


class MachineAssignment(models.Model):

    planting = models.ForeignKey(
        Planting,
        on_delete=models.CASCADE,
        related_name="machines"
    )

    machine = models.ForeignKey(
        Machine,
        on_delete=models.PROTECT
    )

    start_time = models.DateTimeField()

    end_time = models.DateTimeField()

    fuel = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        default=0
    )

    description = models.TextField(blank=True)