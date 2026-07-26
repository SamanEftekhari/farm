from django.db import models


class UserRole(models.TextChoices):
    ADMIN = "admin", "مدیر سیستم"
    MANAGER = "manager", "مدیر مزرعه"
    EXPERT = "expert", "کارشناس"
    FARMER = "farmer", "کشاورز"
    VIEWER = "viewer", "مشاهده کننده"