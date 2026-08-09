from django.contrib import admin

from .models import (
    Crop,
    CropCategory,
    Season,
    CropVariety,
    SeedCompany,
    Seed,
    CropGrowthStage,
    CropDisease,
    CropPest,
)


@admin.register(Crop)
class CropAdmin(admin.ModelAdmin):

    list_display = (
        "code",
        "name",
        "category",
        "season",
        "scientific_name",
        "expected_yield",
        "is_active",
        "created_at",
    )

    search_fields = (
        "code",
        "name",
        "scientific_name",
    )

    list_filter = (
        "category",
        "season",
        "is_active",
    )

    autocomplete_fields = (
        "category",
        "season",
        "diseases",
    )

    readonly_fields = (
        "created_at",
        "updated_at",
    )

    ordering = (
        "name",
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


@admin.register(Season)
class SeasonAdmin(admin.ModelAdmin):

    list_display = (
        "name",
    )

    search_fields = (
        "name",
    )

    ordering = (
        "name",
    )


@admin.register(CropVariety)
class CropVarietyAdmin(admin.ModelAdmin):

    list_display = (
        "code",
        "name",
        "crop",
        "maturity_days",
        "expected_yield",
        "fruit_weight",
        "brix",
        "is_active",
    )

    search_fields = (
        "code",
        "name",
        "crop__name",
    )

    list_filter = (
        "is_active",
        "crop",
    )

    autocomplete_fields = (
        "crop",
    )

    readonly_fields = (
        "created_at",
        "updated_at",
    )

    ordering = (
        "name",
    )


@admin.register(SeedCompany)
class SeedCompanyAdmin(admin.ModelAdmin):

    list_display = (
        "code",
        "name",
        "country",
        "phone",
        "email",
        "is_active",
    )

    search_fields = (
        "code",
        "name",
        "country",
        "phone",
        "email",
    )

    list_filter = (
        "is_active",
        "country",
    )

    readonly_fields = (
        "created_at",
        "updated_at",
    )

    ordering = (
        "name",
    )


@admin.register(Seed)
class SeedAdmin(admin.ModelAdmin):

    list_display = (
        "lot_number",
        "variety",
        "company",
        "production_date",
        "expiry_date",
        "germination",
        "purity",
        "stock",
        "is_active",
    )

    search_fields = (
        "lot_number",
        "serial_number",
        "certificate_number",
        "variety__name",
        "company__name",
    )

    list_filter = (
        "is_active",
        "company",
        "variety__crop",
    )

    autocomplete_fields = (
        "company",
        "variety",
    )

    readonly_fields = (
        "created_at",
        "updated_at",
    )

    ordering = (
        "-production_date",
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

    search_fields = (
        "name",
        "crop__name",
    )

    list_filter = (
        "crop",
    )

    autocomplete_fields = (
        "crop",
    )

    ordering = (
        "crop",
        "order",
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
        "scientific_name",
    )

    list_filter = (
        "is_active",
    )

    ordering = (
        "name",
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

    ordering = (
        "name",
    )