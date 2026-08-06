from django.contrib import admin

# Register your models here.
from django.contrib import admin


from django.contrib import admin


class BaseAdmin(admin.ModelAdmin):

    list_per_page = 30

    save_on_top = True

    readonly_fields = (
        "created_at",
        "updated_at",
    )

    actions_on_top = True

    actions_on_bottom = True