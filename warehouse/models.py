from django.db import models

# Create your models here.
from django.db import models


class Warehouse(models.Model):

    code = models.CharField(max_length=20, unique=True)

    name = models.CharField(max_length=200)

    address = models.TextField(blank=True)

    manager = models.CharField(max_length=200, blank=True)

    description = models.TextField(blank=True)

    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class WarehouseLocation(models.Model):

    warehouse = models.ForeignKey(
        Warehouse,
        on_delete=models.CASCADE,
        related_name="locations"
    )

    code = models.CharField(max_length=30)

    name = models.CharField(max_length=100)

    description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.warehouse.name}-{self.name}"


from operations.models import Harvest


class Stock(models.Model):

    warehouse = models.ForeignKey(
        Warehouse,
        on_delete=models.PROTECT
    )

    harvest = models.ForeignKey(
        Harvest,
        on_delete=models.PROTECT
    )

    quantity = models.DecimalField(
        max_digits=12,
        decimal_places=2
    )

    unit = models.CharField(
        max_length=20,
        default="kg"
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.harvest)


class StockTransaction(models.Model):

    TYPE = (
        ("in", "ورود"),
        ("out", "خروج"),
        ("transfer", "انتقال"),
    )

    stock = models.ForeignKey(
        Stock,
        on_delete=models.CASCADE,
        related_name="transactions"
    )

    transaction_type = models.CharField(
        max_length=20,
        choices=TYPE
    )

    quantity = models.DecimalField(
        max_digits=12,
        decimal_places=2
    )

    transaction_date = models.DateTimeField(
        auto_now_add=True
    )

    description = models.TextField(blank=True)



