from django.contrib import admin

from .models import Crop


@admin.register(Crop)
class CropAdmin(admin.ModelAdmin):

    list_display = (
        "code",
        "name",
        "scientific_name",
        "is_active",
    )

    search_fields = (
        "code",
        "name",
        "scientific_name",
    )

    list_filter = (
        "is_active",
    )

    ordering = (
        "name",
    )

    list_per_page = 25