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
# =========================================================
# SEEDS
# =========================================================

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
    path(
        "api/varieties/<int:crop_id>/",
        views.crop_varieties_api,
        name="crop_varieties_api",
    ),




    # =========================
    # SEED COMPANIES
    # =========================

    path(
        "seed-companies/",
        views.SeedCompanyListView.as_view(),
        name="seed_company_list",
    ),

    path(
        "seed-companies/add/",
        views.SeedCompanyCreateView.as_view(),
        name="seed_company_add",
    ),

    path(
        "seed-companies/<int:pk>/edit/",
        views.SeedCompanyUpdateView.as_view(),
        name="seed_company_edit",
    ),

    path(
        "seed-companies/<int:pk>/delete/",
        views.SeedCompanyDeleteView.as_view(),
        name="seed_company_delete",
    ),


    # =========================
    # VARIETIES API
    # =========================

    path(
        "api/varieties/<int:crop_id>/",
        views.crop_varieties_api,
        name="crop_varieties_api",
    ),

    # ======================================================
    # CROP
    # ======================================================

    path(
        "",
        views.CropListView.as_view(),
        name="crop_list",
    ),

    path(
        "add/",
        views.CropCreateView.as_view(),
        name="crop_create",
    ),

    path(
        "<int:pk>/edit/",
        views.CropUpdateView.as_view(),
        name="crop_update",
    ),

    path(
        "<int:pk>/delete/",
        views.CropDeleteView.as_view(),
        name="crop_delete",
    ),


    # ======================================================
    # VARIETY
    # ======================================================

    path(
        "varieties/",
        views.CropVarietyListView.as_view(),
        name="variety_list",
    ),

    path(
        "varieties/add/",
        views.CropVarietyCreateView.as_view(),
        name="variety_create",
    ),

    path(
        "varieties/<int:pk>/edit/",
        views.CropVarietyUpdateView.as_view(),
        name="variety_update",
    ),

    path(
        "varieties/<int:pk>/delete/",
        views.CropVarietyDeleteView.as_view(),
        name="variety_delete",
    ),


    # ======================================================
    # CATEGORY
    # ======================================================

    path(
        "categories/",
        views.CropCategoryListView.as_view(),
        name="category_list",
    ),

    path(
        "categories/add/",
        views.CropCategoryCreateView.as_view(),
        name="category_create",
    ),


    # ======================================================
    # SEASON
    # ======================================================

    path(
        "seasons/",
        views.SeasonListView.as_view(),
        name="season_list",
    ),

    path(
        "seasons/add/",
        views.SeasonCreateView.as_view(),
        name="season_create",
    ),


    # ======================================================
    # DISEASE
    # ======================================================

    path(
        "diseases/",
        views.CropDiseaseListView.as_view(),
        name="disease_list",
    ),

    path(
        "diseases/add/",
        views.CropDiseaseCreateView.as_view(),
        name="disease_create",
    ),



]