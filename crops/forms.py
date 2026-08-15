from django import forms

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
                    "placeholder": "مثلاً C001",
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
                }
            ),
            "is_active": forms.CheckboxInput(
                attrs={
                    "class": "form-check-input",
                }
            ),
        }