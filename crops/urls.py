from django.urls import path

from . import views


app_name = "crops"


urlpatterns = [
    path(
        "",
        views.crop_list,
        name="crop_list",
    ),

    path(
        "add/",
        views.crop_create,
        name="crop_create",
    ),

    path(
        "<int:pk>/edit/",
        views.crop_update,
        name="crop_update",
    ),

    path(
        "<int:pk>/delete/",
        views.crop_delete,
        name="crop_delete",
    ),
]