from django import forms
from django import forms

from .models import CropVariety

from .models import Crop


class CropForm(forms.ModelForm):

    class Meta:
        model = Crop
        fields = [
            "code",
            "name",
            "scientific_name",
            "description",
            "is_active",
        ]

        widgets = {
            "code": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "مثلاً CROP-001",
                }
            ),
            "name": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "نام محصول",
                }
            ),
            "scientific_name": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "نام علمی",
                }
            ),
            "description": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 4,
                    "placeholder": "توضیحات محصول",
                }
            ),
            "is_active": forms.CheckboxInput(
                attrs={
                    "class": "form-check-input",
                }
            ),
        }

        labels = {
            "code": "کد محصول",
            "name": "نام محصول",
            "scientific_name": "نام علمی",
            "description": "توضیحات",
            "is_active": "فعال",
        }



from django import forms

from .models import Crop, Seed


class SeedForm(forms.ModelForm):

    class Meta:
        model = Seed

        fields = [
            "company",
            "variety",
            "lot_number",
            "serial_number",
            "production_date",
            "expiry_date",
            "package_weight",
            "germination",
            "purity",
            "moisture",
            "purchase_price",
            "stock",
            "certificate_number",
            "notes",
            "is_active",
        ]

        widgets = {
            "company": forms.Select(
                attrs={"class": "form-select"}
            ),

            "variety": forms.Select(
                attrs={"class": "form-select"}
            ),

            "lot_number": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "شماره بچ",
                }
            ),

            "serial_number": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "شماره سریال",
                }
            ),

            "production_date": forms.DateInput(
                attrs={
                    "class": "form-control",
                    "type": "date",
                }
            ),

            "expiry_date": forms.DateInput(
                attrs={
                    "class": "form-control",
                    "type": "date",
                }
            ),

            "package_weight": forms.NumberInput(
                attrs={
                    "class": "form-control",
                    "step": "0.01",
                    "min": "0",
                }
            ),

            "germination": forms.NumberInput(
                attrs={
                    "class": "form-control",
                    "step": "0.01",
                    "min": "0",
                    "max": "100",
                }
            ),

            "purity": forms.NumberInput(
                attrs={
                    "class": "form-control",
                    "step": "0.01",
                    "min": "0",
                    "max": "100",
                }
            ),

            "moisture": forms.NumberInput(
                attrs={
                    "class": "form-control",
                    "step": "0.01",
                    "min": "0",
                    "max": "100",
                }
            ),

            "purchase_price": forms.NumberInput(
                attrs={
                    "class": "form-control",
                    "step": "0.01",
                    "min": "0",
                }
            ),

            "stock": forms.NumberInput(
                attrs={
                    "class": "form-control",
                    "step": "0.01",
                    "min": "0",
                }
            ),

            "certificate_number": forms.TextInput(
                attrs={
                    "class": "form-control",
                }
            ),

            "notes": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 4,
                }
            ),

            "is_active": forms.CheckboxInput(
                attrs={
                    "class": "form-check-input",
                }
            ),
        }


from .models import SeedCompany


class SeedCompanyForm(forms.ModelForm):

    class Meta:
        model = SeedCompany

        fields = [
            "code",
            "name",
            "country",
            "website",
            "email",
            "phone",
            "address",
            "description",
            "is_active",
        ]

        widgets = {
            "code": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "مثلاً SC-001",
                }
            ),
            "name": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "نام شرکت",
                }
            ),
            "country": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "کشور",
                }
            ),
            "website": forms.URLInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "https://example.com",
                }
            ),
            "email": forms.EmailInput(
                attrs={
                    "class": "form-control",
                }
            ),
            "phone": forms.TextInput(
                attrs={
                    "class": "form-control",
                }
            ),
            "address": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 3,
                }
            ),
            "description": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 4,
                }
            ),
            "is_active": forms.CheckboxInput(
                attrs={
                    "class": "form-check-input",
                }
            ),
        }




class CropVarietyForm(forms.ModelForm):

    class Meta:
        model = CropVariety

        fields = [
            "crop",
            "code",
            "name",
            "maturity_days",
            "expected_yield",
            "fruit_weight",
            "brix",
            "disease_resistance",
            "notes",
            "is_active",
        ]

        widgets = {
            "crop": forms.Select(
                attrs={
                    "class": "form-select",
                }
            ),

            "code": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "مثلاً TOM-001",
                }
            ),

            "name": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "نام رقم",
                }
            ),

            "maturity_days": forms.NumberInput(
                attrs={
                    "class": "form-control",
                    "min": "0",
                }
            ),

            "expected_yield": forms.NumberInput(
                attrs={
                    "class": "form-control",
                    "step": "0.01",
                    "min": "0",
                }
            ),

            "fruit_weight": forms.NumberInput(
                attrs={
                    "class": "form-control",
                    "step": "0.01",
                    "min": "0",
                }
            ),

            "brix": forms.NumberInput(
                attrs={
                    "class": "form-control",
                    "step": "0.01",
                    "min": "0",
                }
            ),

            "disease_resistance": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": "3",
                    "placeholder": "مقاومت‌های رقم به بیماری‌ها",
                }
            ),

            "notes": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": "3",
                }
            ),

            "is_active": forms.CheckboxInput(
                attrs={
                    "class": "form-check-input",
                }
            ),
        }