from django.conf import settings
from django.db import models

from common.models import BaseModel


class Farm(BaseModel):
    """
    اطلاعات مزرعه
    """

    FARM_TYPES = (
        ("traditional", "Traditional"),
        ("industrial", "Industrial"),
        ("greenhouse", "Greenhouse"),
        ("warmhouse", "Warmhouse"),
    )

    name = models.CharField(
        max_length=200,
        verbose_name="Farm Name"
    )

    code = models.CharField(
        max_length=30,
        unique=True,
        verbose_name="Code"
    )

    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        related_name="owned_farms",
        verbose_name="Owner"
    )

    project_manager = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="managed_farms",
        verbose_name="Project Manager"
    )

    farm_type = models.CharField(
        max_length=20,
        choices=FARM_TYPES,
        default="traditional",
    )

    province = models.CharField(
        max_length=100,
        blank=True
    )

    city = models.CharField(
        max_length=100,
        blank=True
    )

    address = models.TextField(
        blank=True
    )

    area = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        help_text="Hectare"
    )

    latitude = models.DecimalField(
        max_digits=10,
        decimal_places=7,
        null=True,
        blank=True
    )

    longitude = models.DecimalField(
        max_digits=10,
        decimal_places=7,
        null=True,
        blank=True
    )

    description = models.TextField(
        blank=True
    )

    is_active = models.BooleanField(
        default=True
    )

    class Meta:
        ordering = ["name"]
        verbose_name = "Farm"
        verbose_name_plural = "Farms"

    def __str__(self):
        return self.name


class Block(BaseModel):
    """
    قطعات مزرعه
    """

    farm = models.ForeignKey(
        Farm,
        on_delete=models.CASCADE,
        related_name="blocks"
    )

    name = models.CharField(
        max_length=150
    )

    code = models.CharField(
        max_length=20
    )

    area = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    description = models.TextField(
        blank=True
    )

    class Meta:
        unique_together = ("farm", "code")
        ordering = ["name"]

    def __str__(self):
        return f"{self.farm.name} - {self.name}"


class Field(BaseModel):
    """
    قطعه کشت
    """

    STATUS = (
        ("active", "Active"),
        ("inactive", "Inactive"),
        ("archive", "Archive"),
    )

    block = models.ForeignKey(
        Block,
        on_delete=models.CASCADE,
        related_name="fields"
    )

    name = models.CharField(
        max_length=150
    )

    code = models.CharField(
        max_length=30
    )

    area = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    soil_type = models.CharField(
        max_length=100,
        blank=True
    )

    elevation = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        null=True,
        blank=True
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS,
        default="active"
    )

    description = models.TextField(
        blank=True
    )

    class Meta:
        ordering = ["name"]
        unique_together = ("block", "code")

    def __str__(self):
        return self.name




class FieldPolygon(BaseModel):

    field = models.OneToOneField(
        Field,
        on_delete=models.CASCADE,
        related_name="polygon"
    )

    coordinates = models.JSONField(
        default=list,
        help_text="Leaflet Polygon Coordinates"
    )

    center_lat = models.DecimalField(
        max_digits=10,
        decimal_places=7,
        null=True,
        blank=True
    )

    center_lng = models.DecimalField(
        max_digits=10,
        decimal_places=7,
        null=True,
        blank=True
    )

    zoom = models.PositiveIntegerField(
        default=17
    )

    def __str__(self):
        return f"Polygon : {self.field.name}"


class Crop(BaseModel):
    """
    نوع محصول
    """

    name = models.CharField(
        max_length=150,
        unique=True
    )

    scientific_name = models.CharField(
        max_length=200,
        blank=True
    )

    description = models.TextField(
        blank=True
    )

    is_active = models.BooleanField(
        default=True
    )

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name

class FieldCrop(BaseModel):
    """
    محصول کشت شده در یک قطعه
    """

    STATUS = (
        ("planned", "Planned"),
        ("growing", "Growing"),
        ("harvested", "Harvested"),
        ("finished", "Finished"),
    )

    field = models.ForeignKey(
        Field,
        on_delete=models.CASCADE,
        related_name="crops"
    )

    crop = models.ForeignKey(
        Crop,
        on_delete=models.PROTECT
    )

    crop_year = models.PositiveIntegerField()

    planting_date = models.DateField(
        null=True,
        blank=True
    )

    harvest_date = models.DateField(
        null=True,
        blank=True
    )

    expected_yield = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=True,
        blank=True,
        help_text="Ton"
    )

    actual_yield = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=True,
        blank=True
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS,
        default="planned"
    )

    description = models.TextField(
        blank=True
    )

    class Meta:
        ordering = [
            "-crop_year",
            "field"
        ]

    def __str__(self):
        return f"{self.field} - {self.crop}"