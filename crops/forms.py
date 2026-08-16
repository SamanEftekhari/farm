from django import forms

from .models import (
    Crop,
    CropCategory,
    CropDisease,
    CropVariety,
    Season,
    Seed,
    SeedCompany,
)


# ==========================================================
# BASE BOOTSTRAP FORM
# ==========================================================

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


# ==========================================================
# SEED COMPANY
# ==========================================================

class SeedCompanyForm(BootstrapModelForm):

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

        labels = {
            "code": "کد شرکت",
            "name": "نام شرکت",
            "country": "کشور",
            "website": "وب‌سایت",
            "email": "ایمیل",
            "phone": "تلفن",
            "address": "آدرس",
            "description": "توضیحات",
            "is_active": "فعال",
        }


# ==========================================================
# SEED
# ==========================================================

class SeedForm(BootstrapModelForm):

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

        labels = {
            "company": "شرکت تولیدکننده",
            "variety": "رقم محصول",
            "lot_number": "شماره بچ",
            "serial_number": "شماره سریال",
            "production_date": "تاریخ تولید",
            "expiry_date": "تاریخ انقضا",
            "package_weight": "وزن بسته (کیلوگرم)",
            "germination": "جوانه‌زنی (%)",
            "purity": "خلوص (%)",
            "moisture": "رطوبت (%)",
            "purchase_price": "قیمت خرید",
            "stock": "موجودی",
            "certificate_number": "شماره گواهی",
            "notes": "توضیحات",
            "is_active": "فعال",
        }

        widgets = {
            "production_date": forms.DateInput(
                attrs={
                    "type": "date",
                }
            ),

            "expiry_date": forms.DateInput(
                attrs={
                    "type": "date",
                }
            ),

            "notes": forms.Textarea(
                attrs={
                    "rows": 4,
                }
            ),
        }


# ==========================================================
# CROP CATEGORY
# ==========================================================

class CropCategoryForm(BootstrapModelForm):

    class Meta:

        model = CropCategory

        fields = [
            "name",
            "description",
        ]

        labels = {
            "name": "دسته محصول",
            "description": "توضیحات",
        }

        widgets = {
            "description": forms.Textarea(
                attrs={
                    "rows": 4,
                }
            ),
        }


# ==========================================================
# SEASON
# ==========================================================

class SeasonForm(BootstrapModelForm):

    class Meta:

        model = Season

        fields = [
            "name",
        ]

        labels = {
            "name": "فصل کشت",
        }


# ==========================================================
# CROP DISEASE
# ==========================================================

class CropDiseaseForm(BootstrapModelForm):

    class Meta:

        model = CropDisease

        fields = [
            "code",
            "name",
            "scientific_name",
            "description",
            "prevention",
            "treatment",
            "is_active",
        ]

        labels = {
            "code": "کد بیماری",
            "name": "نام بیماری",
            "scientific_name": "نام علمی",
            "description": "توضیحات",
            "prevention": "روش پیشگیری",
            "treatment": "روش کنترل",
            "is_active": "فعال",
        }

        widgets = {

            "description": forms.Textarea(
                attrs={
                    "rows": 4,
                }
            ),

            "prevention": forms.Textarea(
                attrs={
                    "rows": 4,
                }
            ),

            "treatment": forms.Textarea(
                attrs={
                    "rows": 4,
                }
            ),
        }


# ==========================================================
# CROP
# ==========================================================

class CropForm(BootstrapModelForm):

    class Meta:

        model = Crop

        fields = [
            "category",
            "season",
            "code",
            "name",
            "scientific_name",
            "color",
            "expected_yield",
            "image",
            "description",
            "is_active",
            "diseases",
        ]

        labels = {
            "category": "دسته محصول",
            "season": "فصل کشت",
            "code": "کد محصول",
            "name": "نام محصول",
            "scientific_name": "نام علمی",
            "color": "رنگ محصول",
            "expected_yield": "عملکرد مورد انتظار (تن در هکتار)",
            "image": "تصویر",
            "description": "توضیحات",
            "is_active": "فعال",
            "diseases": "بیماری‌ها",
        }

        widgets = {

            "description": forms.Textarea(
                attrs={
                    "rows": 4,
                }
            ),

            "diseases": forms.SelectMultiple(
                attrs={
                    "class": "form-select",
                }
            ),
        }


# ==========================================================
# CROP VARIETY
# ==========================================================

class CropVarietyForm(BootstrapModelForm):

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

        labels = {
            "crop": "محصول",
            "code": "کد رقم",
            "name": "نام رقم",
            "maturity_days": "دوره رسیدگی (روز)",
            "expected_yield": "عملکرد مورد انتظار (تن در هکتار)",
            "fruit_weight": "میانگین وزن میوه (گرم)",
            "brix": "درجه بریکس",
            "disease_resistance": "مقاومت به بیماری",
            "notes": "توضیحات",
            "is_active": "فعال",
        }

        widgets = {

            "disease_resistance": forms.Textarea(
                attrs={
                    "rows": 4,
                }
            ),

            "notes": forms.Textarea(
                attrs={
                    "rows": 4,
                }
            ),
        }