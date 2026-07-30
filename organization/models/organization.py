from django.db import models

from common.models import AuditModel
from .choices import OrganizationType


class Organization(AuditModel):
    """
    Organization
    """

    name = models.CharField(
        max_length=200,
        verbose_name="نام سازمان",
    )

    short_name = models.CharField(
        max_length=50,
        blank=True,
        verbose_name="نام کوتاه",
    )

    organization_type = models.CharField(
        max_length=20,
        choices=OrganizationType.choices,
        default=OrganizationType.PRIVATE,
        verbose_name="نوع سازمان",
    )

    national_id = models.CharField(
        max_length=20,
        blank=True,
        verbose_name="شناسه ملی",
    )

    economic_code = models.CharField(
        max_length=20,
        blank=True,
        verbose_name="کد اقتصادی",
    )

    manager = models.CharField(
        max_length=150,
        blank=True,
        verbose_name="مدیر",
    )

    phone = models.CharField(
        max_length=30,
        blank=True,
        verbose_name="تلفن",
    )

    mobile = models.CharField(
        max_length=30,
        blank=True,
        verbose_name="موبایل",
    )

    email = models.EmailField(
        blank=True,
    )

    website = models.URLField(
        blank=True,
    )

    address = models.TextField(
        blank=True,
        verbose_name="آدرس",
    )

    logo = models.ImageField(
        upload_to="organizations/",
        blank=True,
        null=True,
    )

    class Meta:
        ordering = ["name"]
        verbose_name = "سازمان"
        verbose_name_plural = "سازمان‌ها"

    def __str__(self):
        return self.name