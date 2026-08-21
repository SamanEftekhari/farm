from django.db import models

# Create your models here.
class FieldCrop(models.Model):
    field = models.ForeignKey(
        "farmland.Field",
        on_delete=models.CASCADE,
        related_name="cultivations",
        verbose_name="زمین",
    )

    crop = models.ForeignKey(
        "crops.Crop",
        on_delete=models.PROTECT,
        related_name="field_crops",
        verbose_name="محصول",
    )

    variety = models.ForeignKey(
        "crops.CropVariety",
        on_delete=models.PROTECT,
        blank=True,
        null=True,
        related_name="field_crops",
        verbose_name="رقم",
    )

    agricultural_year = models.CharField(
        max_length=20,
        verbose_name="سال زراعی",
    )

    cultivated_area = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name="مساحت زیرکشت",
    )

    planting_date = models.CharField(
        max_length=20,
        blank=True,
        verbose_name="تاریخ کاشت",
    )

    planting_density = models.CharField(
        max_length=100,
        blank=True,
        verbose_name="تراکم کاشت",
    )

    planting_method = models.CharField(
        max_length=200,
        blank=True,
        verbose_name="روش کاشت",
    )

    seedling_supplier = models.CharField(
        max_length=200,
        blank=True,
        verbose_name="تأمین‌کننده بذر/نشا",
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
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "کشت زمین"
        verbose_name_plural = "کشت‌های زمین"

    def __str__(self):
        return f"{self.field} - {self.crop}"




class SoilAnalysis(models.Model):
    field_crop = models.ForeignKey(
        FieldCrop,
        on_delete=models.CASCADE,
        related_name="soil_analyses",
        verbose_name="کشت",
    )

    sample_date = models.CharField(
        max_length=20,
        blank=True,
        verbose_name="تاریخ نمونه‌گیری",
    )

    parameter = models.CharField(
        max_length=150,
        verbose_name="پارامتر",
    )

    value = models.CharField(
        max_length=100,
        verbose_name="مقدار",
    )

    unit = models.CharField(
        max_length=50,
        blank=True,
        verbose_name="واحد",
    )

    ideal_range = models.TextField(
        blank=True,
        verbose_name="محدوده ایده‌آل",
    )

    notes = models.TextField(
        blank=True,
        verbose_name="توضیحات",
    )

    def __str__(self):
        return f"{self.parameter} - {self.field_crop}"



class Fertilization(models.Model):
    field_crop = models.ForeignKey(
        FieldCrop,
        on_delete=models.CASCADE,
        related_name="fertilizations",
        verbose_name="کشت",
    )

    date = models.CharField(
        max_length=20,
        verbose_name="تاریخ",
    )

    fertilizer = models.CharField(
        max_length=200,
        verbose_name="نوع کود",
    )

    amount = models.CharField(
        max_length=150,
        verbose_name="مقدار مصرف",
    )

    approved_amount = models.CharField(
        max_length=150,
        blank=True,
        verbose_name="مقدار مصوب",
    )

    application_method = models.CharField(
        max_length=150,
        blank=True,
        verbose_name="روش مصرف",
    )

    notes = models.TextField(
        blank=True,
        verbose_name="توضیحات",
    )

    def __str__(self):
        return f"{self.fertilizer} - {self.field_crop}"



class PestDiseaseControl(models.Model):
    field_crop = models.ForeignKey(
        FieldCrop,
        on_delete=models.CASCADE,
        related_name="pest_controls",
        verbose_name="کشت",
    )

    date = models.CharField(
        max_length=50,
        verbose_name="تاریخ",
    )

    problem_type = models.CharField(
        max_length=150,
        verbose_name="نوع آفت/بیماری",
    )

    control_method = models.CharField(
        max_length=200,
        verbose_name="سم یا روش کنترل",
    )

    amount = models.CharField(
        max_length=150,
        blank=True,
        verbose_name="مقدار مصرف",
    )

    application_method = models.CharField(
        max_length=150,
        blank=True,
        verbose_name="روش اجرا",
    )

    notes = models.TextField(
        blank=True,
        verbose_name="توضیحات",
    )


class Harvest(models.Model):
    field_crop = models.ForeignKey(
        FieldCrop,
        on_delete=models.PROTECT,
        related_name="harvests",
        verbose_name="کشت",
    )

    start_date = models.CharField(
        max_length=20,
        blank=True,
        verbose_name="شروع برداشت",
    )

    end_date = models.CharField(
        max_length=20,
        blank=True,
        verbose_name="پایان برداشت",
    )

    total_quantity = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        default=0,
        verbose_name="مقدار محصول برداشتی",
    )

    quantity_unit = models.CharField(
        max_length=30,
        default="کیلوگرم",
        verbose_name="واحد",
    )

    efficiency = models.DecimalField(
        max_digits=7,
        decimal_places=2,
        blank=True,
        null=True,
        verbose_name="راندمان",
    )

    waste_percent = models.DecimalField(
        max_digits=7,
        decimal_places=2,
        blank=True,
        null=True,
        verbose_name="ضایعات",
    )

    notes = models.TextField(
        blank=True,
        verbose_name="توضیحات",
    )



