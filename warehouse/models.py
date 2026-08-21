from django.db import models


# ==========================================================
# WAREHOUSE
# ==========================================================

class Warehouse(models.Model):

    code = models.CharField(
        max_length=30,
        unique=True,
        editable=False,
        verbose_name="کد انبار",
    )

    name = models.CharField(
        max_length=200,
        verbose_name="نام انبار",
    )

    location = models.CharField(
        max_length=300,
        blank=True,
        verbose_name="محل انبار",
    )

    manager = models.CharField(
        max_length=150,
        blank=True,
        verbose_name="مسئول انبار",
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
        verbose_name = "انبار"
        verbose_name_plural = "انبارها"

    def save(self, *args, **kwargs):

        if not self.code:
            last = (
                Warehouse.objects
                .order_by("-id")
                .first()
            )

            number = last.id + 1 if last else 1

            self.code = f"WH-{number:04d}"

        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.code} - {self.name}"


# ==========================================================
# HARVEST BATCH
# ==========================================================

class HarvestBatch(models.Model):

    code = models.CharField(
        max_length=30,
        unique=True,
        editable=False,
        verbose_name="کد بچ برداشت",
    )

    harvest_date = models.DateField(
        verbose_name="تاریخ برداشت",
    )

    product = models.ForeignKey(
        "crops.Crop",
        on_delete=models.PROTECT,
        related_name="harvest_batches",
        verbose_name="محصول",
    )

    variety = models.ForeignKey(
        "crops.CropVariety",
        on_delete=models.PROTECT,
        related_name="harvest_batches",
        blank=True,
        null=True,
        verbose_name="رقم",
    )

    field = models.ForeignKey(
        "farmland.Field",
        on_delete=models.PROTECT,
        related_name="harvest_batches",
        verbose_name="قطعه زمین",
    )

    quantity = models.DecimalField(
        max_digits=12,
        decimal_places=3,
        default=0,
        verbose_name="مقدار برداشت",
    )

    unit = models.CharField(
        max_length=30,
        default="kg",
        verbose_name="واحد",
    )

    description = models.TextField(
        blank=True,
        verbose_name="توضیحات",
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    class Meta:
        ordering = ["-harvest_date", "-id"]
        verbose_name = "بچ برداشت"
        verbose_name_plural = "بچ‌های برداشت"

    def save(self, *args, **kwargs):

        if not self.code:
            last = (
                HarvestBatch.objects
                .order_by("-id")
                .first()
            )

            number = last.id + 1 if last else 1

            self.code = f"HB-{number:04d}"

        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.code} - {self.product.name}"


# ==========================================================
# QUALITY GRADE
# ==========================================================

class QualityGrade(models.Model):

    code = models.CharField(
        max_length=30,
        unique=True,
        editable=False,
        verbose_name="کد درجه",
    )

    name = models.CharField(
        max_length=100,
        verbose_name="درجه کیفیت",
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
        verbose_name = "درجه کیفیت"
        verbose_name_plural = "درجات کیفیت"

    def save(self, *args, **kwargs):

        if not self.code:
            last = (
                QualityGrade.objects
                .order_by("-id")
                .first()
            )

            number = last.id + 1 if last else 1

            self.code = f"QG-{number:04d}"

        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


# ==========================================================
# INVENTORY LOT
# ==========================================================

class InventoryLot(models.Model):

    code = models.CharField(
        max_length=30,
        unique=True,
        editable=False,
        verbose_name="کد موجودی",
    )

    harvest_batch = models.ForeignKey(
        HarvestBatch,
        on_delete=models.PROTECT,
        related_name="inventory_lots",
        verbose_name="بچ برداشت",
    )

    warehouse = models.ForeignKey(
        Warehouse,
        on_delete=models.PROTECT,
        related_name="inventory_lots",
        verbose_name="انبار",
    )

    quality_grade = models.ForeignKey(
        QualityGrade,
        on_delete=models.PROTECT,
        related_name="inventory_lots",
        verbose_name="درجه کیفیت",
    )

    quantity = models.DecimalField(
        max_digits=12,
        decimal_places=3,
        default=0,
        verbose_name="موجودی",
    )

    unit = models.CharField(
        max_length=30,
        default="kg",
        verbose_name="واحد",
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    updated_at = models.DateTimeField(
        auto_now=True,
    )

    class Meta:
        verbose_name = "موجودی انبار"
        verbose_name_plural = "موجودی انبار"

    def save(self, *args, **kwargs):

        if not self.code:
            last = (
                InventoryLot.objects
                .order_by("-id")
                .first()
            )

            number = last.id + 1 if last else 1

            self.code = f"LOT-{number:04d}"

        super().save(*args, **kwargs)

    def __str__(self):
        return (
            f"{self.code} - "
            f"{self.harvest_batch.product.name} - "
            f"{self.quality_grade.name}"
        )


# ==========================================================
# WAREHOUSE TRANSACTION
# ==========================================================

class WarehouseTransaction(models.Model):

    class TransactionType(models.TextChoices):

        IN = "IN", "ورود"

        OUT = "OUT", "خروج"

        TRANSFER = "TRANSFER", "انتقال"

        QUALITY_CHANGE = "QUALITY_CHANGE", "تغییر درجه کیفیت"

        ADJUSTMENT = "ADJUSTMENT", "اصلاح موجودی"

    code = models.CharField(
        max_length=30,
        unique=True,
        editable=False,
        verbose_name="کد تراکنش",
    )

    inventory_lot = models.ForeignKey(
        InventoryLot,
        on_delete=models.PROTECT,
        related_name="transactions",
        verbose_name="موجودی",
    )

    transaction_type = models.CharField(
        max_length=30,
        choices=TransactionType.choices,
        verbose_name="نوع تراکنش",
    )

    date = models.DateField(
        verbose_name="تاریخ",
    )

    quantity = models.DecimalField(
        max_digits=12,
        decimal_places=3,
        verbose_name="مقدار",
    )

    destination = models.CharField(
        max_length=200,
        blank=True,
        verbose_name="مقصد",
    )

    reference = models.CharField(
        max_length=100,
        blank=True,
        verbose_name="مرجع",
    )

    notes = models.TextField(
        blank=True,
        verbose_name="توضیحات",
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    class Meta:
        ordering = ["-date", "-id"]
        verbose_name = "تراکنش انبار"
        verbose_name_plural = "تراکنش‌های انبار"

    def save(self, *args, **kwargs):

        if not self.code:
            last = (
                WarehouseTransaction.objects
                .order_by("-id")
                .first()
            )

            number = last.id + 1 if last else 1

            self.code = f"TRX-{number:06d}"

        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.code} - {self.get_transaction_type_display()}"


# ==========================================================
# QUALITY CONVERSION
# ==========================================================

class QualityConversion(models.Model):

    code = models.CharField(
        max_length=30,
        unique=True,
        editable=False,
        verbose_name="کد تبدیل",
    )

    inventory_lot = models.ForeignKey(
        InventoryLot,
        on_delete=models.PROTECT,
        related_name="quality_conversions",
        verbose_name="موجودی",
    )

    from_grade = models.ForeignKey(
        QualityGrade,
        on_delete=models.PROTECT,
        related_name="quality_conversion_from",
        verbose_name="درجه اولیه",
    )

    to_grade = models.ForeignKey(
        QualityGrade,
        on_delete=models.PROTECT,
        related_name="quality_conversion_to",
        verbose_name="درجه جدید",
    )

    date = models.DateField(
        verbose_name="تاریخ",
    )

    quantity = models.DecimalField(
        max_digits=12,
        decimal_places=3,
        verbose_name="مقدار",
    )

    reason = models.TextField(
        blank=True,
        verbose_name="علت تغییر",
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    class Meta:
        ordering = ["-date", "-id"]
        verbose_name = "تبدیل کیفیت"
        verbose_name_plural = "تبدیل‌های کیفیت"

    def save(self, *args, **kwargs):

        if not self.code:
            last = (
                QualityConversion.objects
                .order_by("-id")
                .first()
            )

            number = last.id + 1 if last else 1

            self.code = f"QC-{number:06d}"

        super().save(*args, **kwargs)

    def __str__(self):
        return (
            f"{self.code} - "
            f"{self.from_grade} → {self.to_grade}"
        )