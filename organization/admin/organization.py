from django.contrib import admin

from organization.models import Organization


@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):

    list_display = (
        "code",
        "name",
        "organization_type",
        "phone",
        "is_active",
    )

    list_filter = (
        "organization_type",
        "is_active",
    )

    search_fields = (
        "code",
        "name",
        "phone",
        "national_id",
    )

    list_per_page = 30