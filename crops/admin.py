from django.contrib import admin

from common.admin import BaseAdmin

from .models import (
    Crop,
    CropCategory,
    Season,
    CropVariety,
    SeedCompany,
    Seed,
    CropDisease,
    CropPest,
    CropGrowthStage,
)

@admin.register(CropCategory)
class CropCategoryAdmin(admin.ModelAdmin):

    list_display = (
        "name",
    )

    search_fields = (
        "name",
    )

    ordering = (
        "name",
    )


@admin.register(CropGrowthStage)
class CropGrowthStageAdmin(admin.ModelAdmin):

    list_display = (
        "crop",
        "order",
        "name",
        "start_day",
        "end_day",
    )

    list_filter = (
        "crop",
    )

    search_fields = (
        "name",
    )

    autocomplete_fields = (
        "crop",
    )

@admin.register(CropPest)
class CropPestAdmin(admin.ModelAdmin):

    list_display = (
        "code",
        "name",
        "is_active",
    )

    search_fields = (
        "code",
        "name",
    )

    list_filter = (
        "is_active",
    )


@admin.register(CropDisease)
class CropDiseaseAdmin(admin.ModelAdmin):

    list_display = (
        "code",
        "name",
        "scientific_name",
        "is_active",
    )

    search_fields = (
        "code",
        "name",
    )

    list_filter = (
        "is_active",
    )


@admin.register(Seed)
class SeedAdmin(BaseAdmin):

    search_fields = (
        "lot_number",
        "serial_number",
    )

    list_display = (
        "lot_number",
        "company",
        "variety",
        "stock",
    )


@admin.register(Crop)
class CropAdmin(BaseAdmin):

    search_fields = (
        "code",
        "name",
        "scientific_name",
    )

@admin.register(CropVariety)
class CropVarietyAdmin(admin.ModelAdmin):

    search_fields = (
        "code",
        "name",
    )

