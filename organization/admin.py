from django.contrib import admin

from organization.models import Organization


@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "short_name",
        "organization_type",
        "manager",
        "phone",
        "email",
    )

    search_fields = (
        "name",
        "short_name",
        "national_id",
        "economic_code",
        "manager",
        "phone",
        "mobile",
        "email",
    )

    list_filter = (
        "organization_type",
    )

    readonly_fields = (
        "created_by",
        "updated_by",
    )

    fieldsets = (
        (
            "اطلاعات سازمان",
            {
                "fields": (
                    "name",
                    "short_name",
                    "organization_type",
                    "national_id",
                    "economic_code",
                )
            },
        ),
        (
            "اطلاعات تماس",
            {
                "fields": (
                    "manager",
                    "phone",
                    "mobile",
                    "email",
                    "website",
                    "address",
                )
            },
        ),
        (
            "تصویر",
            {
                "fields": (
                    "logo",
                )
            },
        ),
        (
            "اطلاعات ثبت",
            {
                "classes": ("collapse",),
                "fields": (
                    "created_by",
                    "updated_by",
                )
            },
        ),
    )

    ordering = (
        "name",
    )