from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import include, path
from django.views.generic import TemplateView

from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularSwaggerView,
)


urlpatterns = [

    # =========================
    # HOME
    # =========================
    path(
        "",
        TemplateView.as_view(
            template_name="home.html"
        ),
        name="home",
    ),

    # =========================
    # ADMIN
    # =========================
    path(
        "admin/",
        admin.site.urls,
    ),

    # =========================
    # API
    # =========================
    path(
        "api/",
        include("api.urls"),
    ),

    # =========================
    # API SCHEMA
    # =========================
    path(
        "api/schema/",
        SpectacularAPIView.as_view(),
        name="schema",
    ),

    # =========================
    # SWAGGER
    # =========================
    path(
        "api/docs/",
        SpectacularSwaggerView.as_view(
            url_name="schema",
        ),
        name="swagger",
    ),

    # =========================
    # MAPS
    # =========================
    path(
        "maps/",
        include("maps.urls"),
    ),

    # =========================
    # CROPS
    # =========================
    path(
        "crops/",
        include("crops.urls"),
    ),

    # =========================
    # AUTHENTICATION
    # =========================
    path(
        "login/",
        auth_views.LoginView.as_view(
            template_name="registration/login.html",
        ),
        name="login",
    ),

    path(
        "logout/",
        auth_views.LogoutView.as_view(),
        name="logout",
    ),
    path(
        "farmland/",
        include("farmland.urls"),
    ),
    path(
        "inventory/",
         include("inventory.urls"),
    ),
]