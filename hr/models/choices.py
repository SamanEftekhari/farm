from django.db import models


class Gender(models.TextChoices):
    MALE = "MALE", "مرد"
    FEMALE = "FEMALE", "زن"


class EmploymentType(models.TextChoices):
    PERMANENT = "PERMANENT", "رسمی"
    CONTRACT = "CONTRACT", "قراردادی"
    DAILY = "DAILY", "روزمزد"
    SEASONAL = "SEASONAL", "فصلی"
    CONSULTANT = "CONSULTANT", "مشاور"


class EmployeeStatus(models.TextChoices):
    ACTIVE = "ACTIVE", "فعال"
    LEAVE = "LEAVE", "مرخصی"
    SUSPENDED = "SUSPENDED", "تعلیق"
    RETIRED = "RETIRED", "بازنشسته"