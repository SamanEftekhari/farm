from django.db import models

from farmland.models import Field
from crops.models import CropVariety, Seed


class Planting(models.Model):

    STATUS_CHOICES = (
        ("planned", "برنامه‌ریزی شده"),
        ("planted", "کشت شده"),
        ("growing", "در حال رشد"),
        ("finished", "پایان یافته"),
        ("cancelled", "لغو شده"),
    )

    code = models.CharField(
        max_length=30,
        unique=True,
        verbose_name="کد عملیات"
    )

    field = models.ForeignKey(
        Field,
        on_delete=models.PROTECT,
        related_name="plantings",
        verbose_name="قطعه زمین"
    )

    variety = models.ForeignKey(
        CropVariety,
        on_delete=models.PROTECT,
        related_name="plantings",
        verbose_name="رقم"
    )

    seed = models.ForeignKey(
        Seed,
        on_delete=models.PROTECT,
        related_name="plantings",
        verbose_name="بذر"
    )

    planting_date = models.DateField(
        verbose_name="تاریخ کاشت"
    )

    expected_harvest_date = models.DateField(
        null=True,
        blank=True,
        verbose_name="تاریخ پیش‌بینی برداشت"
    )

    cultivated_area = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name="سطح زیر کشت (هکتار)"
    )

    seed_amount = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name="مقدار بذر (کیلوگرم)"
    )

    row_spacing = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        default=0,
        verbose_name="فاصله ردیف (سانتی‌متر)"
    )

    plant_spacing = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        default=0,
        verbose_name="فاصله بوته (سانتی‌متر)"
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="planned",
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
        ordering = ["-planting_date"]
        verbose_name = "عملیات کاشت"
        verbose_name_plural = "عملیات کاشت"

    def __str__(self):
        return self.code