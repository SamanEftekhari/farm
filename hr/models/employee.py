from django.db import models

from common.models import AuditModel

from .choices import (
    Gender,
    EmploymentType,
    EmployeeStatus,
)


class Employee(AuditModel):
    """
    Employee
    """

    first_name = models.CharField(
        max_length=100,
        verbose_name="نام",
    )

    last_name = models.CharField(
        max_length=100,
        verbose_name="نام خانوادگی",
    )

    national_code = models.CharField(
        max_length=10,
        unique=True,
        verbose_name="کد ملی",
    )

    personnel_code = models.CharField(
        max_length=30,
        unique=True,
        verbose_name="کد پرسنلی",
    )

    gender = models.CharField(
        max_length=10,
        choices=Gender.choices,
        default=Gender.MALE,
    )

    mobile = models.CharField(
        max_length=20,
        blank=True,
    )

    phone = models.CharField(
        max_length=20,
        blank=True,
    )

    email = models.EmailField(
        blank=True,
    )

    birth_date = models.DateField(
        null=True,
        blank=True,
    )

    employment_type = models.CharField(
        max_length=20,
        choices=EmploymentType.choices,
        default=EmploymentType.CONTRACT,
    )

    status = models.CharField(
        max_length=20,
        choices=EmployeeStatus.choices,
        default=EmployeeStatus.ACTIVE,
    )

    hire_date = models.DateField(
        null=True,
        blank=True,
    )

    job_title = models.CharField(
        max_length=150,
        blank=True,
        verbose_name="سمت",
    )

    specialization = models.CharField(
        max_length=150,
        blank=True,
        verbose_name="تخصص",
    )

    salary = models.DecimalField(
        max_digits=15,
        decimal_places=2,
        default=0,
    )

    photo = models.ImageField(
        upload_to="employees/",
        null=True,
        blank=True,
    )

    address = models.TextField(
        blank=True,
    )

    emergency_contact = models.CharField(
        max_length=150,
        blank=True,
        verbose_name="شماره تماس اضطراری",
    )

    class Meta:
        ordering = ["last_name", "first_name"]
        verbose_name = "پرسنل"
        verbose_name_plural = "پرسنل"

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.full_name