from django.contrib import admin


class BaseAdmin(admin.ModelAdmin):

    list_per_page = 25

    ordering = ("id",)

    save_on_top = True

    actions_on_top = True

    actions_on_bottom = True

    list_filter = (
        "status",
    )

    readonly_fields = (
        "created_at",
        "updated_at",
    )

    fieldsets = (

        (
            None,
            {
                "fields": ()
            }
        ),

        (
            "اطلاعات سیستم",
            {
                "classes": ("collapse",),
                "fields": (
                    "created_at",
                    "updated_at",
                    "status",
                    "is_deleted",
                )
            }
        ),
    )