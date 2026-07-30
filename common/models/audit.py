from django.conf import settings
from django.db import models

from .code import CodeModel


class AuditModel(CodeModel):
    """
    Tracks who created and last updated the record.
    """

    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="%(class)s_created",
        verbose_name="ایجاد کننده",
    )

    updated_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="%(class)s_updated",
        verbose_name="ویرایش کننده",
    )

    class Meta:
        abstract = True