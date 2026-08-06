from django.db import models


class CropDisease(models.Model):

    code = models.CharField(
        max_length=20,
        unique=True,
        verbose_name="کد بیماری"
    )

    name = models.CharField(
        max_length=200,
        verbose_name="نام بیماری"
    )

    scientific_name = models.CharField(
        max_length=200,
        blank=True,
        verbose_name="نام علمی"
    )

    description = models.TextField(
        blank=True,
        verbose_name="توضیحات"
    )

    prevention = models.TextField(
        blank=True,
        verbose_name="روش پیشگیری"
    )

    treatment = models.TextField(
        blank=True,
        verbose_name="روش کنترل"
    )

    is_active = models.BooleanField(
        default=True
    )

    class Meta:
        ordering = ["name"]
        verbose_name = "بیماری"
        verbose_name_plural = "بیماری‌ها"

    def __str__(self):
        return self.name



class CropCategory(models.Model):
    name = models.CharField(
        max_length=100,
        unique=True,
        verbose_name="دسته محصول"
    )

    description = models.TextField(
        blank=True,
        verbose_name="توضیحات"
    )

    class Meta:
        ordering = ["name"]
        verbose_name = "دسته محصول"
        verbose_name_plural = "دسته محصولات"

    def __str__(self):
        return self.name


class Season(models.Model):
    name = models.CharField(
        max_length=100,
        unique=True,
        verbose_name="فصل کشت"
    )

    class Meta:
        verbose_name = "فصل"
        verbose_name_plural = "فصل‌ها"

    def __str__(self):
        return self.name


class Crop(models.Model):

    category = models.ForeignKey(
        CropCategory,
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        related_name="crops",
        verbose_name="دسته محصول"
    )

    season = models.ForeignKey(
        Season,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="crops",
        verbose_name="فصل کشت"
    )

    code = models.CharField(
        max_length=20,
        unique=True,
        verbose_name="کد محصول"
    )

    name = models.CharField(
        max_length=200,
        verbose_name="نام محصول"
    )

    scientific_name = models.CharField(
        max_length=200,
        blank=True,
        verbose_name="نام علمی"
    )

    color = models.CharField(
        max_length=50,
        blank=True,
        verbose_name="رنگ محصول"
    )

    expected_yield = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0,
        verbose_name="عملکرد مورد انتظار (تن در هکتار)"
    )

    image = models.ImageField(
        upload_to="crops/",
        blank=True,
        null=True,
        verbose_name="تصویر"
    )

    description = models.TextField(
        blank=True,
        verbose_name="توضیحات"
    )

    is_active = models.BooleanField(
        default=True,
        verbose_name="فعال"
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )
    diseases = models.ManyToManyField(
        CropDisease,
        blank=True,
        related_name="crops",
        verbose_name="بیماری‌ها"
    )
    class Meta:
        ordering = ["name"]
        verbose_name = "محصول"
        verbose_name_plural = "محصولات"

    def __str__(self):
        return self.name


class CropVariety(models.Model):

    crop = models.ForeignKey(
        Crop,
        on_delete=models.CASCADE,
        related_name="varieties",
        verbose_name="محصول"
    )

    code = models.CharField(
        max_length=30,
        unique=True,
        verbose_name="کد رقم"
    )

    name = models.CharField(
        max_length=200,
        verbose_name="نام رقم"
    )

    maturity_days = models.PositiveIntegerField(
        default=0,
        verbose_name="دوره رسیدگی (روز)"
    )

    expected_yield = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        default=0,
        verbose_name="عملکرد مورد انتظار (تن در هکتار)"
    )

    fruit_weight = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        default=0,
        verbose_name="میانگین وزن میوه (گرم)"
    )

    brix = models.DecimalField(
        max_digits=4,
        decimal_places=2,
        default=0,
        verbose_name="درجه بریکس"
    )

    disease_resistance = models.TextField(
        blank=True,
        verbose_name="مقاومت به بیماری"
    )

    notes = models.TextField(
        blank=True,
        verbose_name="توضیحات"
    )

    is_active = models.BooleanField(
        default=True,
        verbose_name="فعال"
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        ordering = ["name"]
        verbose_name = "رقم محصول"
        verbose_name_plural = "ارقام محصولات"

    def __str__(self):
        return f"{self.crop.name} - {self.name}"

class SeedCompany(models.Model):

    code = models.CharField(
        max_length=20,
        unique=True,
        verbose_name="کد شرکت"
    )

    name = models.CharField(
        max_length=200,
        verbose_name="نام شرکت"
    )

    country = models.CharField(
        max_length=100,
        blank=True,
        verbose_name="کشور"
    )

    website = models.URLField(
        blank=True,
        verbose_name="وب سایت"
    )

    email = models.EmailField(
        blank=True,
        verbose_name="ایمیل"
    )

    phone = models.CharField(
        max_length=30,
        blank=True,
        verbose_name="تلفن"
    )

    address = models.TextField(
        blank=True,
        verbose_name="آدرس"
    )

    description = models.TextField(
        blank=True,
        verbose_name="توضیحات"
    )

    is_active = models.BooleanField(
        default=True,
        verbose_name="فعال"
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        ordering = ["name"]
        verbose_name = "شرکت تولیدکننده بذر"
        verbose_name_plural = "شرکت‌های تولیدکننده بذر"

    def __str__(self):
        return self.name



class Seed(models.Model):

    company = models.ForeignKey(
        SeedCompany,
        on_delete=models.PROTECT,
        related_name="seeds",
        verbose_name="شرکت"
    )

    variety = models.ForeignKey(
        CropVariety,
        on_delete=models.PROTECT,
        related_name="seeds",
        verbose_name="رقم"
    )

    lot_number = models.CharField(
        max_length=100,
        unique=True,
        verbose_name="شماره بچ"
    )

    serial_number = models.CharField(
        max_length=100,
        blank=True,
        verbose_name="شماره سریال"
    )

    production_date = models.DateField(
        null=True,
        blank=True,
        verbose_name="تاریخ تولید"
    )

    expiry_date = models.DateField(
        null=True,
        blank=True,
        verbose_name="تاریخ انقضا"
    )

    package_weight = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        default=0,
        verbose_name="وزن بسته (کیلوگرم)"
    )

    germination = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        default=0,
        verbose_name="درصد جوانه زنی"
    )

    purity = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        default=0,
        verbose_name="درصد خلوص"
    )

    moisture = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        default=0,
        verbose_name="رطوبت (%)"
    )

    purchase_price = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        default=0,
        verbose_name="قیمت خرید"
    )

    stock = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0,
        verbose_name="موجودی"
    )

    certificate_number = models.CharField(
        max_length=100,
        blank=True,
        verbose_name="شماره گواهی"
    )

    notes = models.TextField(
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
        ordering = ["-production_date"]
        verbose_name = "بذر"
        verbose_name_plural = "بذرها"

    def __str__(self):
        return f"{self.variety} ({self.lot_number})"


class CropGrowthStage(models.Model):

    crop = models.ForeignKey(
        Crop,
        on_delete=models.CASCADE,
        related_name="growth_stages",
        verbose_name="محصول"
    )

    order = models.PositiveSmallIntegerField(
        verbose_name="ترتیب مرحله"
    )

    name = models.CharField(
        max_length=100,
        verbose_name="نام مرحله"
    )

    start_day = models.PositiveIntegerField(
        default=0,
        verbose_name="شروع (روز)"
    )

    end_day = models.PositiveIntegerField(
        default=0,
        verbose_name="پایان (روز)"
    )

    description = models.TextField(
        blank=True,
        verbose_name="توضیحات"
    )

    class Meta:
        ordering = ["crop", "order"]
        unique_together = ("crop", "order")
        verbose_name = "مرحله رشد"
        verbose_name_plural = "مراحل رشد"

    def __str__(self):
        return f"{self.crop.name} - {self.name}"



class CropPest(models.Model):

    code = models.CharField(
        max_length=20,
        unique=True
    )

    name = models.CharField(
        max_length=200
    )

    description = models.TextField(
        blank=True
    )

    control_method = models.TextField(
        blank=True
    )

    is_active = models.BooleanField(
        default=True
    )

    class Meta:
        ordering = ["name"]
        verbose_name = "آفت"
        verbose_name_plural = "آفات"

    def __str__(self):
        return self.name



