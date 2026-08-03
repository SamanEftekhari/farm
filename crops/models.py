from django.db import models


class Crop(models.Model):
    code = models.CharField(
        max_length=20,
        unique=True,
        verbose_name="کد محصول"
    )

    name = models.CharField(
        max_length=200,
        verbose_name="نام محصول"
    )

    scientific_name = models.CharField(
        max_length=200,
        blank=True,
        verbose_name="نام علمی"
    )

    description = models.TextField(
        blank=True
    )

    is_active = models.BooleanField(
        default=True
    )

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["name"]
        verbose_name = "محصول"
        verbose_name_plural = "محصولات"

    def __str__(self):
        return self.name