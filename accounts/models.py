from django.contrib.auth.models import AbstractUser
from django.db import models

from core.models import BaseModel
from .managers import UserManager


class User(AbstractUser, BaseModel):

    email = models.EmailField(unique=True)

    mobile = models.CharField(
        max_length=11,
        unique=True,
        blank=True,
        null=True
    )

    avatar = models.ImageField(
        upload_to="avatars/",
        blank=True,
        null=True
    )

    is_email_verified = models.BooleanField(default=False)

    is_mobile_verified = models.BooleanField(default=False)

    last_ip = models.GenericIPAddressField(
        blank=True,
        null=True
    )

    last_activity = models.DateTimeField(
        blank=True,
        null=True
    )

    objects = UserManager()

    USERNAME_FIELD = "email"

    REQUIRED_FIELDS = ["username"]

    class Meta:
        db_table = "users"

    def __str__(self):
        return self.email

from common.validators import validate_mobile

mobile = models.CharField(
    max_length=11,
    unique=True,
    validators=[validate_mobile],
    blank=True,
    null=True,
)