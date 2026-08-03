from django.contrib import admin

from .models import Farm, Field


@admin.register(Farm)
class FarmAdmin(admin.ModelAdmin):

    list_display = (
        "code",
        "name",
        "company",
        "manager",
        "province",
        "city",
        "area",
        "is_active",
    )

    search_fields = (
        "code",
        "name",
        "company",
    )

    list_filter = (
        "province",
        "city",
        "is_active",
    )

    list_per_page = 30

@admin.register(Field)
class FieldAdmin(admin.ModelAdmin):

    list_display = (
        "code",
        "name",
        "farm",
        "area",
        "soil_type",
        "is_active",
    )

    search_fields = (
        "code",
        "name",
    )

    list_filter = (
        "farm",
        "soil_type",
        "is_active",
    )