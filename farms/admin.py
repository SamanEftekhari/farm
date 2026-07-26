from django.contrib import admin

from .models import (
    Farm,
    Block,
    Field,
    Crop,
    FieldCrop,
)


@admin.register(Farm)
class FarmAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "code",
        "farm_type",
        "owner",
        "area",
        "is_active",
    )

    search_fields = (
        "name",
        "code",
    )

    list_filter = (
        "farm_type",
        "is_active",
    )


@admin.register(Block)
class BlockAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "farm",
        "code",
        "area",
    )

    search_fields = (
        "name",
        "code",
    )


@admin.register(Field)
class FieldAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "block",
        "code",
        "area",
        "status",
    )

    list_filter = (
        "status",
    )

    search_fields = (
        "name",
        "code",
    )


@admin.register(Crop)
class CropAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "scientific_name",
        "is_active",
    )

    search_fields = (
        "name",
        "scientific_name",
    )


@admin.register(FieldCrop)
class FieldCropAdmin(admin.ModelAdmin):

    list_display = (
        "field",
        "crop",
        "crop_year",
        "status",
    )

    list_filter = (
        "crop_year",
        "status",
    )