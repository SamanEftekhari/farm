from django import forms

from .models import (
    Unit,
    Warehouse,
    ProductCategory,
    Product,
    Inventory,
    InventoryTransaction,
)


class BootstrapModelForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields.values():

            if isinstance(field.widget, forms.CheckboxInput):
                field.widget.attrs["class"] = "form-check-input"

            elif isinstance(field.widget, forms.Select):
                field.widget.attrs["class"] = "form-select"

            elif isinstance(field.widget, forms.SelectMultiple):
                field.widget.attrs["class"] = "form-select"

            else:
                field.widget.attrs["class"] = "form-control"


# =========================================================
# UNIT
# =========================================================

class UnitForm(BootstrapModelForm):

    class Meta:
        model = Unit

        fields = [
            "name",
            "symbol",
            "is_active",
        ]

        labels = {
            "name": "نام واحد",
            "symbol": "نماد",
            "is_active": "فعال",
        }


# =========================================================
# WAREHOUSE
# =========================================================

class WarehouseForm(BootstrapModelForm):

    class Meta:
        model = Warehouse

        fields = [
            "name",
            "manager",
            "address",
            "description",
            "is_active",
        ]

        labels = {
            "name": "نام انبار",
            "manager": "مسئول انبار",
            "address": "آدرس",
            "description": "توضیحات",
            "is_active": "فعال",
        }

        widgets = {
            "address": forms.Textarea(
                attrs={
                    "rows": 3,
                }
            ),

            "description": forms.Textarea(
                attrs={
                    "rows": 4,
                }
            ),
        }


# =========================================================
# PRODUCT CATEGORY
# =========================================================

class ProductCategoryForm(BootstrapModelForm):

    class Meta:
        model = ProductCategory

        fields = [
            "name",
            "description",
            "is_active",
        ]

        labels = {
            "name": "نام دسته کالا",
            "description": "توضیحات",
            "is_active": "فعال",
        }

        widgets = {
            "description": forms.Textarea(
                attrs={
                    "rows": 4,
                }
            ),
        }


# =========================================================
# PRODUCT
# =========================================================

class ProductForm(BootstrapModelForm):

    class Meta:
        model = Product

        fields = [
            "name",
            "category",
            "unit",
            "minimum_stock",
            "description",
            "is_active",
        ]

        labels = {
            "name": "نام کالا",
            "category": "دسته کالا",
            "unit": "واحد",
            "minimum_stock": "حداقل موجودی",
            "description": "توضیحات",
            "is_active": "فعال",
        }

        widgets = {
            "minimum_stock": forms.NumberInput(
                attrs={
                    "step": "0.001",
                    "min": "0",
                }
            ),

            "description": forms.Textarea(
                attrs={
                    "rows": 4,
                }
            ),
        }


# =========================================================
# INVENTORY
# =========================================================

class InventoryForm(BootstrapModelForm):

    class Meta:
        model = Inventory

        fields = [
            "warehouse",
            "product",
            "quantity",
        ]

        labels = {
            "warehouse": "انبار",
            "product": "کالا",
            "quantity": "موجودی",
        }

        widgets = {
            "quantity": forms.NumberInput(
                attrs={
                    "step": "0.001",
                    "min": "0",
                }
            ),
        }


# =========================================================
# INVENTORY TRANSACTION
# =========================================================

class InventoryTransactionForm(BootstrapModelForm):

    class Meta:
        model = InventoryTransaction

        fields = [
            "warehouse",
            "product",
            "transaction_type",
            "quantity",
            "unit_price",
            "reference_no",
            "description",
        ]

        labels = {
            "warehouse": "انبار",
            "product": "کالا",
            "transaction_type": "نوع تراکنش",
            "quantity": "مقدار",
            "unit_price": "قیمت واحد",
            "reference_no": "شماره مرجع",
            "description": "توضیحات",
        }

        widgets = {
            "quantity": forms.NumberInput(
                attrs={
                    "step": "0.001",
                    "min": "0",
                }
            ),

            "unit_price": forms.NumberInput(
                attrs={
                    "step": "0.01",
                    "min": "0",
                }
            ),

            "description": forms.Textarea(
                attrs={
                    "rows": 4,
                }
            ),
        }