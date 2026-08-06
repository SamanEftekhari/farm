from django.db import models

from organization.models import Employee
from .planting import Planting


class WorkerAssignment(models.Model):

    planting = models.ForeignKey(
        Planting,
        on_delete=models.CASCADE,
        related_name="workers"
    )

    employee = models.ForeignKey(
        Employee,
        on_delete=models.PROTECT
    )

    work_date = models.DateField()

    hours = models.DecimalField(
        max_digits=5,
        decimal_places=2
    )

    description = models.TextField(blank=True)