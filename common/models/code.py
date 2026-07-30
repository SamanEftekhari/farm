from django.db import models

from .base import BaseModel


class CodeModel(BaseModel):
    """
    Adds a unique code to all major entities.
    """

    code = models.CharField(
        max_length=30,
        unique=True,
        db_index=True,
        verbose_name="کد",
    )

    class Meta:
        abstract = True