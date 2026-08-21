from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    CreateView,
    DetailView,
    UpdateView,
    DeleteView,
)

from .models import Farm, Field
from .forms import FarmForm, FieldForm


# =========================================================
# FARM
# =========================================================

class FarmListView(ListView):

    model = Farm
    context_object_name = "farms"
    template_name = "farmland/farm_list.html"


class FarmCreateView(CreateView):

    model = Farm
    form_class = FarmForm
    template_name = "farmland/farm_form.html"
    success_url = reverse_lazy(
        "farmland:farm_list"
    )

    def form_valid(self, form):

        response = super().form_valid(form)

        messages.success(
            self.request,
            f"مزرعه «{self.object.name}» "
            f"با کد {self.object.code} "
            f"با موفقیت ثبت شد."
        )

        return response


class FarmDetailView(DetailView):

    model = Farm
    context_object_name = "farm"
    template_name = "farmland/farm_detail.html"


class FarmUpdateView(UpdateView):

    model = Farm
    form_class = FarmForm
    context_object_name = "farm"
    template_name = "farmland/farm_form.html"
    success_url = reverse_lazy(
        "farmland:farm_list"
    )


class FarmDeleteView(DeleteView):

    model = Farm
    context_object_name = "farm"
    template_name = "farmland/farm_confirm_delete.html"
    success_url = reverse_lazy(
        "farmland:farm_list"
    )


# =========================================================
# FIELD
# =========================================================

class FieldListView(ListView):

    model = Field
    context_object_name = "fields"
    template_name = "farmland/field_list.html"

    def get_queryset(self):

        return (
            Field.objects
            .select_related("farm")
            .order_by("farm__name", "name")
        )


class FieldCreateView(CreateView):

    model = Field
    form_class = FieldForm
    template_name = "farmland/field_form.html"
    success_url = reverse_lazy(
        "farmland:field_list"
    )


class FieldDetailView(DetailView):

    model = Field
    context_object_name = "field"
    template_name = "farmland/field_detail.html"


class FieldUpdateView(UpdateView):

    model = Field
    form_class = FieldForm
    context_object_name = "field"
    template_name = "farmland/field_form.html"
    success_url = reverse_lazy(
        "farmland:field_list"
    )


class FieldDeleteView(DeleteView):

    model = Field
    context_object_name = "field"
    template_name = "farmland/field_confirm_delete.html"
    success_url = reverse_lazy(
        "farmland:field_list"
    )