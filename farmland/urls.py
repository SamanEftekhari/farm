from django.urls import path

from . import views


app_name = "farmland"


urlpatterns = [

    # ======================================================
    # FARM
    # ======================================================

    path(
        "",
        views.FarmListView.as_view(),
        name="farm_list",
    ),

    path(
        "add/",
        views.FarmCreateView.as_view(),
        name="farm_create",
    ),

    path(
        "<int:pk>/",
        views.FarmDetailView.as_view(),
        name="farm_detail",
    ),

    path(
        "<int:pk>/edit/",
        views.FarmUpdateView.as_view(),
        name="farm_update",
    ),

    path(
        "<int:pk>/delete/",
        views.FarmDeleteView.as_view(),
        name="farm_delete",
    ),

]