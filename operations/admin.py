from django.contrib import admin

# Register your models here.
from django.contrib import admin

from common.admin import BaseAdmin

from .models import (
    Planting,
    Harvest,
)

class HarvestInline(admin.TabularInline):

    model = Harvest

    extra = 0

    show_change_link = True


@admin.register(Planting)
class PlantingAdmin(BaseAdmin):

    list_display = (
        "code",
        "field",
        "variety",
        "seed",
        "planting_date",
        "expected_harvest_date",
        "cultivated_area",
        "status",
    )

    search_fields = (
        "code",
        "field__name",
        "variety__name",
    )

    list_filter = (
        "status",
        "planting_date",
        "field",
    )

    autocomplete_fields = (
        "field",
        "variety",
        "seed",
    )

    date_hierarchy = "planting_date"

    inlines = [
        HarvestInline,
    ]



@admin.register(Harvest)
class HarvestAdmin(BaseAdmin):

    list_display = (
        "code",
        "planting",
        "harvest_date",
        "total_weight",
        "premium_weight",
        "grade1_weight",
        "grade2_weight",
        "rejected_weight",
        "status",
    )

    search_fields = (
        "code",
        "planting__code",
    )

    list_filter = (
        "status",
        "harvest_date",
    )

    autocomplete_fields = (
        "planting",
    )

    date_hierarchy = "harvest_date"