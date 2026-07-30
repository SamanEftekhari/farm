from django.db import models


class BaseModel(models.Model):
    """
    Base Model
    """

    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Location(BaseModel):
    """
    Geographic Location
    """

    name = models.CharField(
        max_length=150,
        verbose_name="نام"
    )

    latitude = models.DecimalField(
        max_digits=10,
        decimal_places=7,
        verbose_name="عرض جغرافیایی"
    )

    longitude = models.DecimalField(
        max_digits=10,
        decimal_places=7,
        verbose_name="طول جغرافیایی"
    )

    altitude = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        null=True,
        blank=True,
        verbose_name="ارتفاع"
    )

    address = models.TextField(
        blank=True,
        verbose_name="آدرس"
    )

    description = models.TextField(
        blank=True,
        verbose_name="توضیحات"
    )

    class Meta:
        verbose_name = "موقعیت مکانی"
        verbose_name_plural = "موقعیت‌های مکانی"
        ordering = ["name"]

    def __str__(self):
        return self.name