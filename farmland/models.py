from django.db import models


class Farm(models.Model):
    code = models.CharField(
        max_length=20,
        unique=True,
        verbose_name="کد مزرعه"
    )

    name = models.CharField(
        max_length=200,
        verbose_name="نام مزرعه"
    )

    company = models.CharField(
        max_length=200,
        blank=True,
        verbose_name="شرکت"
    )

    manager = models.CharField(
        max_length=150,
        blank=True,
        verbose_name="مدیر مزرعه"
    )

    area = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0,
        verbose_name="مساحت (هکتار)"
    )

    province = models.CharField(
        max_length=100,
        blank=True,
        verbose_name="استان"
    )

    city = models.CharField(
        max_length=100,
        blank=True,
        verbose_name="شهر"
    )

    address = models.TextField(
        blank=True,
        verbose_name="آدرس"
    )

    latitude = models.DecimalField(
        max_digits=10,
        decimal_places=7,
        blank=True,
        null=True
    )

    longitude = models.DecimalField(
        max_digits=10,
        decimal_places=7,
        blank=True,
        null=True
    )

    description = models.TextField(
        blank=True,
        verbose_name="توضیحات"
    )

    is_active = models.BooleanField(
        default=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        ordering = ["name"]
        verbose_name = "مزرعه"
        verbose_name_plural = "مزارع"

    def __str__(self):
        return self.name


from django.db import models


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
        verbose_name="کد قطعه",
    )

    name = models.CharField(
        max_length=200,
        verbose_name="نام قطعه",
    )

    area = models.DecimalField(
        max_digits=10,
        decimal_places=2,
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
    )

    longitude = models.DecimalField(
        max_digits=10,
        decimal_places=7,
        blank=True,
        null=True,
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
    )

    description = models.TextField(
        blank=True,
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

    def __str__(self):
        return f"{self.farm} - {self.name}"


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
    )

    is_active = models.BooleanField(
        default=True,
    )

    def __str__(self):
        return self.name


class Well(models.Model):

    field = models.ForeignKey(
        Field,
        on_delete=models.CASCADE,
        related_name="wells",
    )

    code = models.CharField(
        max_length=30,
        unique=True,
    )

    name = models.CharField(
        max_length=100,
    )

    depth = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        default=0,
    )

    water_level = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        default=0,
    )

    latitude = models.DecimalField(
        max_digits=10,
        decimal_places=7,
        blank=True,
        null=True,
    )

    longitude = models.DecimalField(
        max_digits=10,
        decimal_places=7,
        blank=True,
        null=True,
    )

    active = models.BooleanField(
        default=True,
    )

    def __str__(self):
        return self.name


class Reservoir(models.Model):

    field = models.ForeignKey(
        Field,
        on_delete=models.CASCADE,
        related_name="reservoirs",
    )

    code = models.CharField(
        max_length=30,
        unique=True,
    )

    name = models.CharField(
        max_length=100,
    )

    capacity = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        default=0,
    )

    current_volume = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        default=0,
    )

    latitude = models.DecimalField(
        max_digits=10,
        decimal_places=7,
        blank=True,
        null=True,
    )

    longitude = models.DecimalField(
        max_digits=10,
        decimal_places=7,
        blank=True,
        null=True,
    )

    active = models.BooleanField(
        default=True,
    )

    def __str__(self):
        return self.name


