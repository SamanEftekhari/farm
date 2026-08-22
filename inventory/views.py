from django.shortcuts import render

# Create your views here.
from django.contrib import messages
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
    DetailView,
)

from .models import (
    Warehouse,
    Unit,
    ProductCategory,
    Product,
    Inventory,
    InventoryTransaction,
)

from .forms import (
    WarehouseForm,
    UnitForm,
    ProductCategoryForm,
    ProductForm,
    InventoryForm,
    InventoryTransactionForm,
)


# =========================================================
# WAREHOUSE
# =========================================================

class WarehouseListView(ListView):
    model = Warehouse
    template_name = "inventory/warehouse_list.html"
    context_object_name = "warehouses"


class WarehouseDetailView(DetailView):
    model = Warehouse
    template_name = "inventory/warehouse_detail.html"
    context_object_name = "warehouse"


class WarehouseCreateView(CreateView):
    model = Warehouse
    form_class = WarehouseForm
    template_name = "inventory/warehouse_form.html"
    success_url = reverse_lazy("inventory:warehouse_list")

    def form_valid(self, form):
        messages.success(
            self.request,
            "انبار با موفقیت ثبت شد."
        )
        return super().form_valid(form)


class WarehouseUpdateView(UpdateView):
    model = Warehouse
    form_class = WarehouseForm
    template_name = "inventory/warehouse_form.html"
    success_url = reverse_lazy("inventory:warehouse_list")

    def form_valid(self, form):
        messages.success(
            self.request,
            "اطلاعات انبار با موفقیت ویرایش شد."
        )
        return super().form_valid(form)


class WarehouseDeleteView(DeleteView):
    model = Warehouse
    template_name = "inventory/confirm_delete.html"
    success_url = reverse_lazy("inventory:warehouse_list")

    def form_valid(self, form):
        messages.success(
            self.request,
            "انبار حذف شد."
        )
        return super().form_valid(form)


# =========================================================
# UNIT
# =========================================================

class UnitListView(ListView):
    model = Unit
    template_name = "inventory/unit_list.html"
    context_object_name = "units"


class UnitCreateView(CreateView):
    model = Unit
    form_class = UnitForm
    template_name = "inventory/unit_form.html"
    success_url = reverse_lazy("inventory:unit_list")


class UnitUpdateView(UpdateView):
    model = Unit
    form_class = UnitForm
    template_name = "inventory/unit_form.html"
    success_url = reverse_lazy("inventory:unit_list")


# =========================================================
# PRODUCT CATEGORY
# =========================================================

class ProductCategoryListView(ListView):
    model = ProductCategory
    template_name = "inventory/category_list.html"
    context_object_name = "categories"


class ProductCategoryCreateView(CreateView):
    model = ProductCategory
    form_class = ProductCategoryForm
    template_name = "inventory/category_form.html"
    success_url = reverse_lazy("inventory:category_list")


class ProductCategoryUpdateView(UpdateView):
    model = ProductCategory
    form_class = ProductCategoryForm
    template_name = "inventory/category_form.html"
    success_url = reverse_lazy("inventory:category_list")


# =========================================================
# PRODUCT
# =========================================================

class ProductListView(ListView):
    model = Product
    template_name = "inventory/product_list.html"
    context_object_name = "products"


class ProductDetailView(DetailView):
    model = Product
    template_name = "inventory/product_detail.html"
    context_object_name = "product"


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = "inventory/product_form.html"
    success_url = reverse_lazy("inventory:product_list")


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    template_name = "inventory/product_form.html"
    success_url = reverse_lazy("inventory:product_list")


# =========================================================
# INVENTORY
# =========================================================

class InventoryListView(ListView):
    model = Inventory
    template_name = "inventory/inventory_list.html"
    context_object_name = "inventories"

    def get_queryset(self):
        return (
            Inventory.objects
            .select_related(
                "warehouse",
                "product",
                "product__unit",
            )
            .order_by(
                "warehouse__name",
                "product__name",
            )
        )


class InventoryCreateView(CreateView):
    model = Inventory
    form_class = InventoryForm
    template_name = "inventory/inventory_form.html"
    success_url = reverse_lazy("inventory:inventory_list")


class InventoryUpdateView(UpdateView):
    model = Inventory
    form_class = InventoryForm
    template_name = "inventory/inventory_form.html"
    success_url = reverse_lazy("inventory:inventory_list")


# =========================================================
# TRANSACTIONS
# =========================================================

class TransactionListView(ListView):
    model = InventoryTransaction
    template_name = "inventory/transaction_list.html"
    context_object_name = "transactions"

    def get_queryset(self):
        return (
            InventoryTransaction.objects
            .select_related(
                "warehouse",
                "product",
                "product__unit",
            )
            .order_by("-transaction_date")
        )


class TransactionCreateView(CreateView):
    model = InventoryTransaction
    form_class = InventoryTransactionForm
    template_name = "inventory/transaction_form.html"
    success_url = reverse_lazy("inventory:transaction_list")

    def form_valid(self, form):

        response = super().form_valid(form)

        transaction = self.object

        inventory, created = Inventory.objects.get_or_create(
            warehouse=transaction.warehouse,
            product=transaction.product,
            defaults={
                "quantity": 0,
            },
        )

        if transaction.transaction_type == "IN":
            inventory.quantity += transaction.quantity

        elif transaction.transaction_type == "OUT":
            inventory.quantity -= transaction.quantity

        inventory.save()

        messages.success(
            self.request,
            "تراکنش انبار با موفقیت ثبت شد."
        )

        return response