from django.db import models

from .planting import Planting


class Harvest(models.Model):

    STATUS_CHOICES = (
        ("draft", "پیش نویس"),
        ("confirmed", "تایید شده"),
        ("closed", "بسته شده"),
    )

    code = models.CharField(
        max_length=30,
        unique=True,
        verbose_name="کد برداشت"
    )

    planting = models.ForeignKey(
        Planting,
        on_delete=models.PROTECT,
        related_name="harvests",
        verbose_name="عملیات کاشت"
    )

    harvest_date = models.DateField(
        verbose_name="تاریخ برداشت"
    )

    total_weight = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        default=0,
        verbose_name="وزن کل (کیلوگرم)"
    )

    grade1_weight = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        default=0,
        verbose_name="درجه یک"
    )

    grade2_weight = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        default=0,
        verbose_name="درجه دو"
    )

    rejected_weight = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        default=0,
        verbose_name="خارج از درجه بندی"
    )

    premium_weight = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        default=0,
        verbose_name="درجه ممتاز"
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="draft",
        verbose_name="وضعیت"
    )

    notes = models.TextField(
        blank=True,
        verbose_name="توضیحات"
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        ordering = ["-harvest_date"]
        verbose_name = "برداشت"
        verbose_name_plural = "برداشت‌ها"

    def __str__(self):
        return self.code