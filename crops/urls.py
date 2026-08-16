from django.urls import path

from . import views


app_name = "crops"


urlpatterns = [
    path(
        "",
        views.crop_list,
        name="list",
    ),

    path(
        "add/",
        views.crop_create,
        name="create",
    ),

    path(
        "<int:pk>/",
        views.crop_detail,
        name="detail",
    ),

    path(
        "<int:pk>/edit/",
        views.crop_update,
        name="update",
    ),

    path(
        "<int:pk>/delete/",
        views.crop_delete,
        name="delete",
    ),
# =========================
    # SEED
    # =========================

    path(
        "seeds/",
        views.seed_list,
        name="seed_list",
    ),

    path(
        "seeds/add/",
        views.seed_create,
        name="seed_create",
    ),

    path(
        "seeds/<int:pk>/",
        views.seed_detail,
        name="seed_detail",
    ),

    path(
        "seeds/<int:pk>/edit/",
        views.seed_update,
        name="seed_update",
    ),

    path(
        "seeds/<int:pk>/delete/",
        views.seed_delete,
        name="seed_delete",
    ),
# =========================
# SEED COMPANIES
# =========================

    path(
       "seed-companies/",
        views.seed_company_list,
        name="seed_company_list",
    ),

    path(
        "seed-companies/add/",
        views.seed_company_create,
        name="seed_company_create",
    ),

    path(
        "seed-companies/<int:pk>/",
        views.seed_company_detail,
        name="seed_company_detail",
    ),

    path(
        "seed-companies/<int:pk>/edit/",
        views.seed_company_update,
        name="seed_company_update",
    ),

    path(
        "seed-companies/<int:pk>/delete/",
        views.seed_company_delete,
        name="seed_company_delete",
    ),
# =========================================================
# CROP VARIETIES
# =========================================================

    path(
        "varieties/",
        views.crop_variety_list,
        name="crop_variety_list",
    ),

    path(
        "varieties/add/",
        views.crop_variety_create,
        name="crop_variety_create",
    ),

    path(
        "varieties/<int:pk>/",
        views.crop_variety_detail,
        name="crop_variety_detail",
    ),

    path(
        "varieties/<int:pk>/edit/",
        views.crop_variety_update,
        name="crop_variety_update",
    ),

    path(
        "varieties/<int:pk>/delete/",
        views.crop_variety_delete,
        name="crop_variety_delete",
    ),


]