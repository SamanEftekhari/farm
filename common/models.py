from django.conf import settings
from django.db import models


class TimeStampModel(models.Model):
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="تاریخ ایجاد",
    )

    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="آخرین بروزرسانی",
    )

    class Meta:
        abstract = True


class CodeModel(models.Model):
    code = models.CharField(
        max_length=30,
        unique=True,
        verbose_name="کد",
    )

    class Meta:
        abstract = True


class AuditModel(models.Model):
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="%(class)s_created",
        verbose_name="ایجاد کننده",
    )

    updated_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="%(class)s_updated",
        verbose_name="ویرایش کننده",
    )

    class Meta:
        abstract = True


class NameModel(models.Model):
    name = models.CharField(
        max_length=200,
        verbose_name="نام",
    )

    description = models.TextField(
        blank=True,
        verbose_name="توضیحات",
    )

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class SoftDeleteModel(models.Model):
    is_deleted = models.BooleanField(
        default=False,
        verbose_name="حذف شده",
    )

    class Meta:
        abstract = True


class StatusModel(models.Model):
    is_active = models.BooleanField(
        default=True,
        verbose_name="فعال",
    )

    class Meta:
        abstract = True


class BaseModel(
    CodeModel,
    TimeStampModel,
    AuditModel,
    StatusModel,
    SoftDeleteModel,
):
    class Meta:
        abstract = True