from django.urls import path

from . import views


app_name = "inventory"


urlpatterns = [

    # =========================
    # WAREHOUSE
    # =========================

    path(
        "",
        views.WarehouseListView.as_view(),
        name="warehouse_list",
    ),

    path(
        "add/",
        views.WarehouseCreateView.as_view(),
        name="warehouse_create",
    ),

    path(
        "<int:pk>/",
        views.WarehouseDetailView.as_view(),
        name="warehouse_detail",
    ),

    path(
        "<int:pk>/edit/",
        views.WarehouseUpdateView.as_view(),
        name="warehouse_update",
    ),

    path(
        "<int:pk>/delete/",
        views.WarehouseDeleteView.as_view(),
        name="warehouse_delete",
    ),


    # =========================
    # UNITS
    # =========================

    path(
        "units/",
        views.UnitListView.as_view(),
        name="unit_list",
    ),

    path(
        "units/add/",
        views.UnitCreateView.as_view(),
        name="unit_create",
    ),

    path(
        "units/<int:pk>/edit/",
        views.UnitUpdateView.as_view(),
        name="unit_update",
    ),


    # =========================
    # CATEGORIES
    # =========================

    path(
        "categories/",
        views.ProductCategoryListView.as_view(),
        name="category_list",
    ),

    path(
        "categories/add/",
        views.ProductCategoryCreateView.as_view(),
        name="category_create",
    ),

    path(
        "categories/<int:pk>/edit/",
        views.ProductCategoryUpdateView.as_view(),
        name="category_update",
    ),


    # =========================
    # PRODUCTS
    # =========================

    path(
        "products/",
        views.ProductListView.as_view(),
        name="product_list",
    ),

    path(
        "products/add/",
        views.ProductCreateView.as_view(),
        name="product_create",
    ),

    path(
        "products/<int:pk>/",
        views.ProductDetailView.as_view(),
        name="product_detail",
    ),

    path(
        "products/<int:pk>/edit/",
        views.ProductUpdateView.as_view(),
        name="product_update",
    ),


    # =========================
    # INVENTORY
    # =========================

    path(
        "stock/",
        views.InventoryListView.as_view(),
        name="inventory_list",
    ),

    path(
        "stock/add/",
        views.InventoryCreateView.as_view(),
        name="inventory_create",
    ),

    path(
        "stock/<int:pk>/edit/",
        views.InventoryUpdateView.as_view(),
        name="inventory_update",
    ),


    # =========================
    # TRANSACTIONS
    # =========================

    path(
        "transactions/",
        views.TransactionListView.as_view(),
        name="transaction_list",
    ),

    path(
        "transactions/add/",
        views.TransactionCreateView.as_view(),
        name="transaction_create",
    ),
]