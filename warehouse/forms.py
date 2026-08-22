from django import forms
from .models import (
    Warehouse,
    HarvestBatch,
    QualityGrade,
    InventoryLot,
    WarehouseTransaction,
    QualityConversion,
)


# ==========================================================
# Bootstrap Base Form
# ==========================================================

class BootstrapModelForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields.values():

            if isinstance(field.widget, forms.CheckboxInput):
                field.widget.attrs["class"] = "form-check-input"

            elif isinstance(field.widget, forms.Select):
                field.widget.attrs["class"] = "form-select"

            else:
                field.widget.attrs["class"] = "form-control"


# ==========================================================
# Warehouse
# ==========================================================

class WarehouseForm(BootstrapModelForm):

    class Meta:

        model = Warehouse

        fields = [
            "name",
            "location",
            "manager",
            "description",
            "is_active",
        ]

        widgets = {
            "description": forms.Textarea(attrs={"rows": 3}),
        }


# ==========================================================
# Harvest Batch
# ==========================================================

class HarvestBatchForm(BootstrapModelForm):

    class Meta:

        model = HarvestBatch

        fields = [
            "harvest_date",
            "product",
            "variety",
            "field",
            "quantity",
            "unit",
            "description",
        ]

        widgets = {
            "harvest_date": forms.DateInput(
                attrs={"type": "date"}
            ),
            "description": forms.Textarea(attrs={"rows": 3}),
        }


# ==========================================================
# Quality Grade
# ==========================================================

class QualityGradeForm(BootstrapModelForm):

    class Meta:

        model = QualityGrade

        fields = [
            "name",
            "description",
            "is_active",
        ]

        widgets = {
            "description": forms.Textarea(attrs={"rows": 3}),
        }


# ==========================================================
# Inventory Lot
# ==========================================================

class InventoryLotForm(BootstrapModelForm):

    class Meta:

        model = InventoryLot

        fields = [
            "harvest_batch",
            "warehouse",
            "quality_grade",
            "quantity",
            "unit",
        ]


# ==========================================================
# Warehouse Transaction
# ==========================================================

class WarehouseTransactionForm(BootstrapModelForm):

    class Meta:

        model = WarehouseTransaction

        fields = [
            "inventory_lot",
            "transaction_type",
            "date",
            "quantity",
            "destination",
            "reference",
            "notes",
        ]

        widgets = {
            "date": forms.DateInput(
                attrs={"type": "date"}
            ),
            "notes": forms.Textarea(attrs={"rows": 3}),
        }


# ==========================================================
# Quality Conversion
# ==========================================================

class QualityConversionForm(BootstrapModelForm):

    class Meta:

        model = QualityConversion

        fields = [
            "inventory_lot",
            "from_grade",
            "to_grade",
            "date",
            "quantity",
            "reason",
        ]

        widgets = {
            "date": forms.DateInput(
                attrs={"type": "date"}
            ),
            "reason": forms.Textarea(attrs={"rows": 3}),
        }