from django.db import models

from .timestamp import TimeStampedModel


class BaseModel(TimeStampedModel):
    """
    Base model for all ASIGI FARM models.
    """

    is_active = models.BooleanField(
        default=True,
        verbose_name="فعال",
        db_index=True,
    )

    description = models.TextField(
        blank=True,
        verbose_name="توضیحات",
    )

    class Meta:
        abstract = True