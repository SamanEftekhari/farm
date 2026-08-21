from django.db import models


# ==========================================================
# FARM
# ==========================================================

class Farm(models.Model):

    code = models.CharField(
        max_length=20,
        unique=True,
        editable=False,
        verbose_name="کد مزرعه",
    )

    name = models.CharField(
        max_length=200,
        verbose_name="نام مزرعه",
    )

    company = models.CharField(
        max_length=200,
        blank=True,
        verbose_name="شرکت",
    )

    manager = models.CharField(
        max_length=150,
        blank=True,
        verbose_name="مدیر مزرعه",
    )

    area = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0,
        verbose_name="مساحت (هکتار)",
    )

    province = models.CharField(
        max_length=100,
        blank=True,
        verbose_name="استان",
    )

    city = models.CharField(
        max_length=100,
        blank=True,
        verbose_name="شهر",
    )

    address = models.TextField(
        blank=True,
        verbose_name="آدرس",
    )

    latitude = models.DecimalField(
        max_digits=10,
        decimal_places=7,
        blank=True,
        null=True,
        verbose_name="عرض جغرافیایی",
    )

    longitude = models.DecimalField(
        max_digits=10,
        decimal_places=7,
        blank=True,
        null=True,
        verbose_name="طول جغرافیایی",
    )

    description = models.TextField(
        blank=True,
        verbose_name="توضیحات",
    )

    is_active = models.BooleanField(
        default=True,
        verbose_name="فعال",
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    updated_at = models.DateTimeField(
        auto_now=True,
    )

    class Meta:
        ordering = ["name"]
        verbose_name = "مزرعه"
        verbose_name_plural = "مزارع"

    def save(self, *args, **kwargs):

        if not self.code:
            last_farm = (
                Farm.objects
                .order_by("-id")
                .first()
            )

            next_number = (
                last_farm.id + 1
                if last_farm
                else 1
            )

            self.code = f"FARM-{next_number:04d}"

        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.code} - {self.name}"


# ==========================================================
# FIELD
# ==========================================================

class Field(models.Model):

    farm = models.ForeignKey(
        Farm,
        on_delete=models.CASCADE,
        related_name="fields",
        verbose_name="مزرعه",
    )

    code = models.CharField(
        max_length=30,
        unique=True,
        editable=False,
        verbose_name="کد قطعه",
    )

    name = models.CharField(
        max_length=200,
        verbose_name="نام قطعه",
    )

    area = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0,
        verbose_name="مساحت (هکتار)",
    )

    soil_type = models.CharField(
        max_length=100,
        blank=True,
        verbose_name="نوع خاک",
    )

    irrigation_type = models.CharField(
        max_length=100,
        blank=True,
        verbose_name="نوع آبیاری",
    )

    latitude = models.DecimalField(
        max_digits=10,
        decimal_places=7,
        blank=True,
        null=True,
        verbose_name="عرض جغرافیایی",
    )

    longitude = models.DecimalField(
        max_digits=10,
        decimal_places=7,
        blank=True,
        null=True,
        verbose_name="طول جغرافیایی",
    )

    elevation = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        blank=True,
        null=True,
        verbose_name="ارتفاع از سطح دریا",
    )

    is_active = models.BooleanField(
        default=True,
        verbose_name="فعال",
    )

    description = models.TextField(
        blank=True,
        verbose_name="توضیحات",
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    updated_at = models.DateTimeField(
        auto_now=True,
    )

    class Meta:
        ordering = ["name"]
        verbose_name = "قطعه زمین"
        verbose_name_plural = "قطعات زمین"

    def save(self, *args, **kwargs):

        if not self.code:
            last_field = (
                Field.objects
                .order_by("-id")
                .first()
            )

            next_number = (
                last_field.id + 1
                if last_field
                else 1
            )

            self.code = f"FIELD-{next_number:04d}"

        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.code} - {self.name}"


# ==========================================================
# GREENHOUSE
# ==========================================================

class Greenhouse(models.Model):

    field = models.ForeignKey(
        Field,
        on_delete=models.CASCADE,
        related_name="greenhouses",
        verbose_name="قطعه زمین",
    )

    code = models.CharField(
        max_length=30,
        unique=True,
        editable=False,
        verbose_name="کد گلخانه",
    )

    name = models.CharField(
        max_length=200,
        verbose_name="نام گلخانه",
    )

    area = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0,
        verbose_name="مساحت",
    )

    greenhouse_type = models.CharField(
        max_length=100,
        blank=True,
        verbose_name="نوع گلخانه",
    )

    description = models.TextField(
        blank=True,
        verbose_name="توضیحات",
    )

    is_active = models.BooleanField(
        default=True,
        verbose_name="فعال",
    )

    class Meta:
        ordering = ["name"]
        verbose_name = "گلخانه"
        verbose_name_plural = "گلخانه‌ها"

    def save(self, *args, **kwargs):

        if not self.code:
            last_greenhouse = (
                Greenhouse.objects
                .order_by("-id")
                .first()
            )

            next_number = (
                last_greenhouse.id + 1
                if last_greenhouse
                else 1
            )

            self.code = f"GH-{next_number:04d}"

        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.code} - {self.name}"


# ==========================================================
# WELL
# ==========================================================

class Well(models.Model):

    field = models.ForeignKey(
        Field,
        on_delete=models.CASCADE,
        related_name="wells",
        verbose_name="قطعه زمین",
    )

    code = models.CharField(
        max_length=30,
        unique=True,
        editable=False,
        verbose_name="کد چاه",
    )

    name = models.CharField(
        max_length=100,
        verbose_name="نام چاه",
    )

    depth = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        default=0,
        verbose_name="عمق",
    )

    water_level = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        default=0,
        verbose_name="سطح آب",
    )

    latitude = models.DecimalField(
        max_digits=10,
        decimal_places=7,
        blank=True,
        null=True,
        verbose_name="عرض جغرافیایی",
    )

    longitude = models.DecimalField(
        max_digits=10,
        decimal_places=7,
        blank=True,
        null=True,
        verbose_name="طول جغرافیایی",
    )

    active = models.BooleanField(
        default=True,
        verbose_name="فعال",
    )

    class Meta:
        ordering = ["name"]
        verbose_name = "چاه"
        verbose_name_plural = "چاه‌ها"

    def save(self, *args, **kwargs):

        if not self.code:
            last_well = (
                Well.objects
                .order_by("-id")
                .first()
            )

            next_number = (
                last_well.id + 1
                if last_well
                else 1
            )

            self.code = f"WELL-{next_number:04d}"

        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.code} - {self.name}"


# ==========================================================
# RESERVOIR
# ==========================================================

class Reservoir(models.Model):

    field = models.ForeignKey(
        Field,
        on_delete=models.CASCADE,
        related_name="reservoirs",
        verbose_name="قطعه زمین",
    )

    code = models.CharField(
        max_length=30,
        unique=True,
        editable=False,
        verbose_name="کد مخزن",
    )

    name = models.CharField(
        max_length=100,
        verbose_name="نام مخزن",
    )

    capacity = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        default=0,
        verbose_name="ظرفیت",
    )

    current_volume = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        default=0,
        verbose_name="حجم فعلی",
    )

    latitude = models.DecimalField(
        max_digits=10,
        decimal_places=7,
        blank=True,
        null=True,
        verbose_name="عرض جغرافیایی",
    )

    longitude = models.DecimalField(
        max_digits=10,
        decimal_places=7,
        blank=True,
        null=True,
        verbose_name="طول جغرافیایی",
    )

    active = models.BooleanField(
        default=True,
        verbose_name="فعال",
    )

    class Meta:
        ordering = ["name"]
        verbose_name = "مخزن"
        verbose_name_plural = "مخازن"

    def save(self, *args, **kwargs):

        if not self.code:
            last_reservoir = (
                Reservoir.objects
                .order_by("-id")
                .first()
            )

            next_number = (
                last_reservoir.id + 1
                if last_reservoir
                else 1
            )

            self.code = f"RES-{next_number:04d}"

        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.code} - {self.name}"