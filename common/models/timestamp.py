from django.db import models


class TimeStampedModel(models.Model):
    """
    Abstract model that stores creation and update timestamps.
    """

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="تاریخ ایجاد",
        db_index=True,
    )

    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="آخرین بروزرسانی",
    )

    class Meta:
        abstract = True