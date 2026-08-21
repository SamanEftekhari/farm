from django import forms

from .models import Farm, Field


# =========================================================
# BOOTSTRAP FORM
# =========================================================

class BootstrapModelForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)

        for field in self.fields.values():

            if isinstance(
                field.widget,
                forms.CheckboxInput
            ):
                field.widget.attrs["class"] = "form-check-input"

            elif isinstance(
                field.widget,
                forms.Select
            ):
                field.widget.attrs["class"] = "form-select"

            else:
                field.widget.attrs["class"] = "form-control"


# =========================================================
# FARM
# =========================================================

class FarmForm(BootstrapModelForm):

    class Meta:

        model = Farm

        fields = [
            "name",
            "company",
            "manager",
            "area",
            "province",
            "city",
            "address",
            "latitude",
            "longitude",
            "description",
            "is_active",
        ]

        labels = {
            "name": "نام مزرعه",
            "company": "شرکت",
            "manager": "مدیر مزرعه",
            "area": "مساحت (هکتار)",
            "province": "استان",
            "city": "شهر",
            "address": "آدرس",
            "latitude": "عرض جغرافیایی",
            "longitude": "طول جغرافیایی",
            "description": "توضیحات",
            "is_active": "فعال",
        }

        widgets = {

            "area": forms.NumberInput(
                attrs={
                    "step": "0.01",
                    "min": "0",
                }
            ),

            "latitude": forms.NumberInput(
                attrs={
                    "step": "0.0000001",
                }
            ),

            "longitude": forms.NumberInput(
                attrs={
                    "step": "0.0000001",
                }
            ),

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
# FIELD
# =========================================================

class FieldForm(BootstrapModelForm):

    class Meta:

        model = Field

        fields = [
            "farm",
            "name",
            "area",
            "soil_type",
            "irrigation_type",
            "latitude",
            "longitude",
            "elevation",
            "is_active",
            "description",
        ]

        labels = {
            "farm": "مزرعه",
            "name": "نام قطعه",
            "area": "مساحت (هکتار)",
            "soil_type": "نوع خاک",
            "irrigation_type": "نوع آبیاری",
            "latitude": "عرض جغرافیایی",
            "longitude": "طول جغرافیایی",
            "elevation": "ارتفاع از سطح دریا",
            "is_active": "فعال",
            "description": "توضیحات",
        }

        widgets = {

            "area": forms.NumberInput(
                attrs={
                    "step": "0.01",
                    "min": "0",
                }
            ),

            "latitude": forms.NumberInput(
                attrs={
                    "step": "0.0000001",
                }
            ),

            "longitude": forms.NumberInput(
                attrs={
                    "step": "0.0000001",
                }
            ),

            "elevation": forms.NumberInput(
                attrs={
                    "step": "0.01",
                }
            ),

            "description": forms.Textarea(
                attrs={
                    "rows": 4,
                }
            ),
        }