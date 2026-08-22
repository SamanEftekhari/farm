from django.db import models

# Create your models here.
from django.db import models


# =========================================================
# UNIT
# =========================================================

class Unit(models.Model):

    code = models.CharField(
        max_length=20,
        unique=True,
        verbose_name="کد واحد",
    )

    name = models.CharField(
        max_length=100,
        unique=True,
        verbose_name="نام واحد",
    )

    symbol = models.CharField(
        max_length=20,
        blank=True,
        verbose_name="نماد",
    )

    is_active = models.BooleanField(
        default=True,
        verbose_name="فعال",
    )

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["name"]
        verbose_name = "واحد اندازه‌گیری"
        verbose_name_plural = "واحدهای اندازه‌گیری"


# =========================================================
# WAREHOUSE
# =========================================================

class Warehouse(models.Model):

    code = models.CharField(
        max_length=20,
        unique=True,
        editable=False,
        verbose_name="کد انبار",
    )

    name = models.CharField(
        max_length=200,
        verbose_name="نام انبار",
    )

    manager = models.CharField(
        max_length=150,
        blank=True,
        verbose_name="مسئول انبار",
    )

    address = models.TextField(
        blank=True,
        verbose_name="آدرس",
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

    def save(self, *args, **kwargs):

        if not self.code:
            last = Warehouse.objects.order_by("-id").first()

            number = (
                last.id + 1
                if last
                else 1
            )

            self.code = f"WH-{number:04d}"

        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.code} - {self.name}"

    class Meta:
        ordering = ["name"]
        verbose_name = "انبار"
        verbose_name_plural = "انبارها"


# =========================================================
# PRODUCT CATEGORY
# =========================================================

class ProductCategory(models.Model):

    code = models.CharField(
        max_length=20,
        unique=True,
        editable=False,
        verbose_name="کد دسته",
    )

    name = models.CharField(
        max_length=150,
        unique=True,
        verbose_name="نام دسته",
    )

    description = models.TextField(
        blank=True,
        verbose_name="توضیحات",
    )

    is_active = models.BooleanField(
        default=True,
        verbose_name="فعال",
    )

    def save(self, *args, **kwargs):

        if not self.code:
            last = ProductCategory.objects.order_by("-id").first()

            number = (
                last.id + 1
                if last
                else 1
            )

            self.code = f"CAT-{number:04d}"

        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["name"]
        verbose_name = "دسته کالا"
        verbose_name_plural = "دسته‌های کالا"


# =========================================================
# PRODUCT
# =========================================================

class Product(models.Model):

    code = models.CharField(
        max_length=30,
        unique=True,
        editable=False,
        verbose_name="کد کالا",
    )

    name = models.CharField(
        max_length=200,
        verbose_name="نام کالا",
    )

    category = models.ForeignKey(
        ProductCategory,
        on_delete=models.PROTECT,
        related_name="products",
        verbose_name="دسته کالا",
    )

    unit = models.ForeignKey(
        Unit,
        on_delete=models.PROTECT,
        related_name="products",
        verbose_name="واحد",
    )

    minimum_stock = models.DecimalField(
        max_digits=14,
        decimal_places=3,
        default=0,
        verbose_name="حداقل موجودی",
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

    def save(self, *args, **kwargs):

        if not self.code:
            last = Product.objects.order_by("-id").first()

            number = (
                last.id + 1
                if last
                else 1
            )

            self.code = f"PRD-{number:06d}"

        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.code} - {self.name}"

    class Meta:
        ordering = ["name"]
        verbose_name = "کالا"
        verbose_name_plural = "کالاها"


# =========================================================
# INVENTORY
# =========================================================

class Inventory(models.Model):

    warehouse = models.ForeignKey(
        Warehouse,
        on_delete=models.CASCADE,
        related_name="inventories",
        verbose_name="انبار",
    )

    product = models.ForeignKey(
        Product,
        on_delete=models.PROTECT,
        related_name="inventories",
        verbose_name="کالا",
    )

    quantity = models.DecimalField(
        max_digits=14,
        decimal_places=3,
        default=0,
        verbose_name="موجودی",
    )

    updated_at = models.DateTimeField(
        auto_now=True,
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["warehouse", "product"],
                name="unique_warehouse_product",
            )
        ]

        verbose_name = "موجودی"
        verbose_name_plural = "موجودی‌ها"

    def __str__(self):
        return f"{self.warehouse} - {self.product}"


# =========================================================
# INVENTORY TRANSACTION
# =========================================================

class InventoryTransaction(models.Model):

    TRANSACTION_TYPES = [
        ("IN", "ورود"),
        ("OUT", "خروج"),
        ("TRANSFER", "انتقال"),
    ]

    code = models.CharField(
        max_length=30,
        unique=True,
        editable=False,
        verbose_name="کد تراکنش",
    )

    warehouse = models.ForeignKey(
        Warehouse,
        on_delete=models.PROTECT,
        related_name="transactions",
        verbose_name="انبار",
    )

    product = models.ForeignKey(
        Product,
        on_delete=models.PROTECT,
        related_name="transactions",
        verbose_name="کالا",
    )

    transaction_type = models.CharField(
        max_length=10,
        choices=TRANSACTION_TYPES,
        verbose_name="نوع تراکنش",
    )

    quantity = models.DecimalField(
        max_digits=14,
        decimal_places=3,
        verbose_name="مقدار",
    )

    unit_price = models.DecimalField(
        max_digits=16,
        decimal_places=2,
        default=0,
        verbose_name="قیمت واحد",
    )

    transaction_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name="تاریخ تراکنش",
    )

    reference_no = models.CharField(
        max_length=100,
        blank=True,
        verbose_name="شماره مرجع",
    )

    description = models.TextField(
        blank=True,
        verbose_name="توضیحات",
    )

    def save(self, *args, **kwargs):

        if not self.code:
            last = (
                InventoryTransaction.objects
                .order_by("-id")
                .first()
            )

            number = (
                last.id + 1
                if last
                else 1
            )

            self.code = f"TRX-{number:06d}"

        super().save(*args, **kwargs)

    def __str__(self):
        return self.code

    class Meta:
        ordering = ["-transaction_date"]
        verbose_name = "تراکنش انبار"
        verbose_name_plural = "تراکنش‌های انبار"