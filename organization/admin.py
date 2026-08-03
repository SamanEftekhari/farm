from django.contrib import admin

from .models import Organization


@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):

    list_display = (
        "code",
        "name",
        "short_name",
        "organization_type",
        "manager",
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
        "short_name",
        "manager",
        "phone",
        "national_id",
    )

    readonly_fields = (
        "created_at",
        "updated_at",
    )

    fieldsets = (

        ("اطلاعات اصلی", {
            "fields": (
                "code",
                "name",
                "short_name",
                "organization_type",
                "logo",
            )
        }),

        ("اطلاعات مدیریتی", {
            "fields": (
                "manager",
                "national_id",
                "economic_code",
            )
        }),

        ("اطلاعات تماس", {
            "fields": (
                "phone",
                "mobile",
                "email",
                "website",
                "address",
            )
        }),

        ("سایر", {
            "fields": (
                "description",
                "is_active",
            )
        }),

        ("سیستمی", {
            "classes": ("collapse",),
            "fields": (
                "created_at",
                "updated_at",
                "created_by",
                "updated_by",
            )
        }),

    )