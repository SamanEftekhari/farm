from django.db import models

# Create your models here.
from django.db import models


class QualityStandard(models.Model):

    code = models.CharField(
        max_length=20,
        unique=True
    )

    name = models.CharField(
        max_length=200
    )

    description = models.TextField(blank=True)

    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


from operations.models import Harvest


class QualityInspection(models.Model):

    STATUS = (
        ("pending", "در انتظار"),
        ("approved", "تایید"),
        ("rejected", "رد شده"),
    )

    harvest = models.ForeignKey(
        Harvest,
        on_delete=models.CASCADE,
        related_name="inspections"
    )

    inspection_date = models.DateField()

    inspector = models.CharField(
        max_length=200
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS,
        default="pending"
    )

    notes = models.TextField(blank=True)

    def __str__(self):
        return self.harvest.code


class QualityResult(models.Model):

    inspection = models.ForeignKey(
        QualityInspection,
        on_delete=models.CASCADE,
        related_name="results"
    )

    standard = models.ForeignKey(
        QualityStandard,
        on_delete=models.PROTECT
    )

    value = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    min_value = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0
    )

    max_value = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0
    )

    passed = models.BooleanField(default=True)

    def __str__(self):
        return self.standard.name



class QualityGrade(models.Model):

    inspection = models.ForeignKey(
        QualityInspection,
        on_delete=models.CASCADE,
        related_name="grades"
    )

    grade = models.CharField(
        max_length=30,
        choices=(
            ("special", "ممتاز"),
            ("grade1", "درجه یک"),
            ("grade2", "درجه دو"),
            ("grade3", "درجه سه"),
            ("waste", "ضایعات"),
        )
    )

    weight = models.DecimalField(
        max_digits=12,
        decimal_places=2
    )

    package_count = models.PositiveIntegerField(default=0)

    notes = models.TextField(blank=True)

    def __str__(self):
        return self.grade

