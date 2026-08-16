from .forms import CropVarietyForm
from .models import CropVariety
from .forms import CropForm, SeedForm, SeedCompanyForm
from .models import Crop, Seed, SeedCompany
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    ListView,
    UpdateView,
)

from .forms import (
    CropCategoryForm,
    CropDiseaseForm,
    CropForm,
    CropVarietyForm,
    SeasonForm,
)

from .models import (
    Crop,
    CropCategory,
    CropDisease,
    CropVariety,
    Season,
)
from .models import SeedCompany
from .models import Seed
from .models import Crop, CropVariety
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
)
from .models import SeedCompany

@login_required
def crop_list(request):
    crops = Crop.objects.all()

    return render(
        request,
        "crops/crop_list.html",
        {
            "crops": crops,
        },
    )


@login_required
def crop_create(request):

    if request.method == "POST":
        form = CropForm(request.POST)

        if form.is_valid():
            crop = form.save()

            messages.success(
                request,
                f"محصول «{crop.name}» با موفقیت ثبت شد.",
            )

            return redirect("crops:list")

    else:
        form = CropForm()

    return render(
        request,
        "crops/crop_form.html",
        {
            "form": form,
            "title": "ثبت محصول جدید",
            "button_text": "ثبت محصول",
        },
    )


@login_required
def crop_detail(request, pk):

    crop = get_object_or_404(
        Crop,
        pk=pk,
    )

    return render(
        request,
        "crops/crop_detail.html",
        {
            "crop": crop,
        },
    )


@login_required
def crop_update(request, pk):

    crop = get_object_or_404(
        Crop,
        pk=pk,
    )

    if request.method == "POST":
        form = CropForm(
            request.POST,
            instance=crop,
        )

        if form.is_valid():
            crop = form.save()

            messages.success(
                request,
                f"محصول «{crop.name}» با موفقیت ویرایش شد.",
            )

            return redirect(
                "crops:detail",
                pk=crop.pk,
            )

    else:
        form = CropForm(
            instance=crop,
        )

    return render(
        request,
        "crops/crop_form.html",
        {
            "form": form,
            "crop": crop,
            "title": "ویرایش محصول",
            "button_text": "ذخیره تغییرات",
        },
    )


@login_required
def crop_delete(request, pk):

    crop = get_object_or_404(
        Crop,
        pk=pk,
    )

    if request.method == "POST":

        name = crop.name

        crop.delete()

        messages.success(
            request,
            f"محصول «{name}» حذف شد.",
        )

        return redirect("crops:list")

    return render(
        request,
        "crops/crop_confirm_delete.html",
        {
            "crop": crop,
        },
    )


@login_required
def seed_list(request):
    seeds = Seed.objects.select_related(
        "company",
        "variety",
    ).all()

    return render(
        request,
        "crops/seed_list.html",
        {
            "seeds": seeds,
        },
    )


@login_required
def seed_create(request):

    if request.method == "POST":

        form = SeedForm(request.POST)

        if form.is_valid():

            seed = form.save()

            messages.success(
                request,
                f"بذر با شماره بچ «{seed.lot_number}» با موفقیت ثبت شد.",
            )

            return redirect("crops:seed_list")

    else:
        form = SeedForm()

    return render(
        request,
        "crops/seed_form.html",
        {
            "form": form,
            "title": "ثبت بذر جدید",
            "button_text": "ثبت بذر",
        },
    )


@login_required
def seed_detail(request, pk):

    seed = get_object_or_404(
        Seed.objects.select_related(
            "company",
            "variety",
        ),
        pk=pk,
    )

    return render(
        request,
        "crops/seed_detail.html",
        {
            "seed": seed,
        },
    )


@login_required
def seed_update(request, pk):

    seed = get_object_or_404(
        Seed,
        pk=pk,
    )

    if request.method == "POST":

        form = SeedForm(
            request.POST,
            instance=seed,
        )

        if form.is_valid():

            seed = form.save()

            messages.success(
                request,
                f"بذر «{seed.lot_number}» با موفقیت ویرایش شد.",
            )

            return redirect(
                "crops:seed_detail",
                pk=seed.pk,
            )

    else:

        form = SeedForm(
            instance=seed,
        )

    return render(
        request,
        "crops/seed_form.html",
        {
            "form": form,
            "seed": seed,
            "title": "ویرایش بذر",
            "button_text": "ذخیره تغییرات",
        },
    )


@login_required
def seed_delete(request, pk):

    seed = get_object_or_404(
        Seed,
        pk=pk,
    )

    if request.method == "POST":

        lot_number = seed.lot_number

        seed.delete()

        messages.success(
            request,
            f"بذر «{lot_number}» حذف شد.",
        )

        return redirect("crops:seed_list")

    return render(
        request,
        "crops/seed_confirm_delete.html",
        {
            "seed": seed,
        },
    )


@login_required
def seed_company_list(request):

    companies = SeedCompany.objects.all()

    return render(
        request,
        "crops/seed_company_list.html",
        {
            "companies": companies,
        },
    )


@login_required
def seed_company_create(request):

    if request.method == "POST":

        form = SeedCompanyForm(request.POST)

        if form.is_valid():

            company = form.save()

            messages.success(
                request,
                f"شرکت «{company.name}» با موفقیت ثبت شد.",
            )

            return redirect(
                "crops:seed_company_list"
            )

    else:

        form = SeedCompanyForm()

    return render(
        request,
        "crops/seed_company_form.html",
        {
            "form": form,
            "title": "ثبت شرکت تولیدکننده بذر",
            "button_text": "ثبت شرکت",
        },
    )


@login_required
def seed_company_detail(request, pk):

    company = get_object_or_404(
        SeedCompany,
        pk=pk,
    )

    return render(
        request,
        "crops/seed_company_detail.html",
        {
            "company": company,
        },
    )


@login_required
def seed_company_update(request, pk):

    company = get_object_or_404(
        SeedCompany,
        pk=pk,
    )

    if request.method == "POST":

        form = SeedCompanyForm(
            request.POST,
            instance=company,
        )

        if form.is_valid():

            company = form.save()

            messages.success(
                request,
                f"شرکت «{company.name}» با موفقیت ویرایش شد.",
            )

            return redirect(
                "crops:seed_company_detail",
                pk=company.pk,
            )

    else:

        form = SeedCompanyForm(
            instance=company,
        )

    return render(
        request,
        "crops/seed_company_form.html",
        {
            "form": form,
            "company": company,
            "title": "ویرایش شرکت تولیدکننده بذر",
            "button_text": "ذخیره تغییرات",
        },
    )


@login_required
def seed_company_delete(request, pk):

    company = get_object_or_404(
        SeedCompany,
        pk=pk,
    )

    if request.method == "POST":

        name = company.name

        company.delete()

        messages.success(
            request,
            f"شرکت «{name}» حذف شد.",
        )

        return redirect(
            "crops:seed_company_list"
        )

    return render(
        request,
        "crops/seed_company_confirm_delete.html",
        {
            "company": company,
        },
    )


@login_required
def crop_variety_list(request):

    varieties = (
        CropVariety.objects
        .select_related("crop")
        .all()
    )

    return render(
        request,
        "crops/crop_variety_list.html",
        {
            "varieties": varieties,
        },
    )


@login_required
def crop_variety_create(request):

    if request.method == "POST":

        form = CropVarietyForm(request.POST)

        if form.is_valid():

            variety = form.save()

            messages.success(
                request,
                f"رقم «{variety.name}» با موفقیت ثبت شد.",
            )

            return redirect(
                "crops:crop_variety_list"
            )

    else:

        form = CropVarietyForm()

    return render(
        request,
        "crops/crop_variety_form.html",
        {
            "form": form,
            "title": "ثبت رقم محصول",
            "button_text": "ثبت رقم",
        },
    )


@login_required
def crop_variety_detail(request, pk):

    variety = get_object_or_404(
        CropVariety.objects.select_related("crop"),
        pk=pk,
    )

    return render(
        request,
        "crops/crop_variety_detail.html",
        {
            "variety": variety,
        },
    )


@login_required
def crop_variety_update(request, pk):

    variety = get_object_or_404(
        CropVariety,
        pk=pk,
    )

    if request.method == "POST":

        form = CropVarietyForm(
            request.POST,
            instance=variety,
        )

        if form.is_valid():

            variety = form.save()

            messages.success(
                request,
                f"رقم «{variety.name}» با موفقیت ویرایش شد.",
            )

            return redirect(
                "crops:crop_variety_detail",
                pk=variety.pk,
            )

    else:

        form = CropVarietyForm(
            instance=variety,
        )

    return render(
        request,
        "crops/crop_variety_form.html",
        {
            "form": form,
            "variety": variety,
            "title": "ویرایش رقم محصول",
            "button_text": "ذخیره تغییرات",
        },
    )


@login_required
def crop_variety_delete(request, pk):

    variety = get_object_or_404(
        CropVariety,
        pk=pk,
    )

    if request.method == "POST":

        name = variety.name

        variety.delete()

        messages.success(
            request,
            f"رقم «{name}» حذف شد.",
        )

        return redirect(
            "crops:crop_variety_list"
        )

    return render(
        request,
        "crops/crop_variety_confirm_delete.html",
        {
            "variety": variety,
        },
    )




@login_required
def seed_list(request):
    seeds = (
        Seed.objects
        .select_related("company", "variety", "variety__crop")
        .all()
    )

    return render(
        request,
        "crops/seed_list.html",
        {
            "seeds": seeds,
        },
    )


@login_required
def seed_create(request):
    if request.method == "POST":
        form = SeedForm(request.POST)

        if form.is_valid():
            seed = form.save()

            messages.success(
                request,
                f"بذر «{seed.lot_number}» با موفقیت ثبت شد.",
            )

            return redirect("crops:seed_list")

    else:
        form = SeedForm()

    return render(
        request,
        "crops/seed_form.html",
        {
            "form": form,
            "title": "ثبت بذر جدید",
            "button_text": "ثبت بذر",
        },
    )


@login_required
def seed_detail(request, pk):
    seed = get_object_or_404(
        Seed.objects.select_related(
            "company",
            "variety",
            "variety__crop",
        ),
        pk=pk,
    )

    return render(
        request,
        "crops/seed_detail.html",
        {
            "seed": seed,
        },
    )


@login_required
def seed_update(request, pk):
    seed = get_object_or_404(Seed, pk=pk)

    if request.method == "POST":
        form = SeedForm(
            request.POST,
            instance=seed,
        )

        if form.is_valid():
            seed = form.save()

            messages.success(
                request,
                f"بذر «{seed.lot_number}» با موفقیت ویرایش شد.",
            )

            return redirect(
                "crops:seed_detail",
                pk=seed.pk,
            )

    else:
        form = SeedForm(instance=seed)

    return render(
        request,
        "crops/seed_form.html",
        {
            "form": form,
            "seed": seed,
            "title": "ویرایش بذر",
            "button_text": "ذخیره تغییرات",
        },
    )


@login_required
def seed_delete(request, pk):
    seed = get_object_or_404(Seed, pk=pk)

    if request.method == "POST":
        lot_number = seed.lot_number

        seed.delete()

        messages.success(
            request,
            f"بذر «{lot_number}» حذف شد.",
        )

        return redirect("crops:seed_list")

    return render(
        request,
        "crops/seed_confirm_delete.html",
        {
            "seed": seed,
        },
    )


def crop_varieties_api(request, crop_id):
    crop = get_object_or_404(Crop, pk=crop_id)

    varieties = (
        CropVariety.objects
        .filter(crop=crop, is_active=True)
        .order_by("name")
    )

    data = [
        {
            "id": variety.id,
            "name": variety.name,
            "code": variety.code,
        }
        for variety in varieties
    ]

    return JsonResponse(data, safe=False)






class SeedCompanyListView(LoginRequiredMixin, ListView):

    model = SeedCompany
    template_name = "crops/seed_company_list.html"
    context_object_name = "companies"

    def get_queryset(self):
        return SeedCompany.objects.all().order_by("name")


class SeedCompanyCreateView(LoginRequiredMixin, CreateView):

    model = SeedCompany
    form_class = SeedCompanyForm
    template_name = "crops/seed_company_form.html"
    success_url = reverse_lazy("crops:seed_company_list")

    extra_context = {
        "title": "ثبت شرکت تولیدکننده بذر",
        "button_text": "ثبت شرکت",
    }


class SeedCompanyUpdateView(LoginRequiredMixin, UpdateView):

    model = SeedCompany
    form_class = SeedCompanyForm
    template_name = "crops/seed_company_form.html"
    success_url = reverse_lazy("crops:seed_company_list")

    extra_context = {
        "title": "ویرایش شرکت تولیدکننده بذر",
        "button_text": "ذخیره تغییرات",
    }


class SeedCompanyDeleteView(LoginRequiredMixin, DeleteView):

    model = SeedCompany
    template_name = "crops/seed_company_confirm_delete.html"
    success_url = reverse_lazy("crops:seed_company_list")




# ==========================================================
# CROP
# ==========================================================

class CropListView(LoginRequiredMixin, ListView):

    model = Crop
    template_name = "crops/crop_list.html"
    context_object_name = "crops"

    def get_queryset(self):
        return (
            Crop.objects
            .select_related("category", "season")
            .prefetch_related("diseases")
        )


class CropCreateView(LoginRequiredMixin, CreateView):

    model = Crop
    form_class = CropForm
    template_name = "crops/crop_form.html"
    success_url = reverse_lazy("crops:crop_list")

    extra_context = {
        "title": "ثبت محصول جدید",
        "button_text": "ثبت محصول",
    }


class CropUpdateView(LoginRequiredMixin, UpdateView):

    model = Crop
    form_class = CropForm
    template_name = "crops/crop_form.html"
    success_url = reverse_lazy("crops:crop_list")

    extra_context = {
        "title": "ویرایش محصول",
        "button_text": "ذخیره تغییرات",
    }


class CropDeleteView(LoginRequiredMixin, DeleteView):

    model = Crop
    template_name = "crops/crop_confirm_delete.html"
    success_url = reverse_lazy("crops:crop_list")


# ==========================================================
# CROP VARIETY
# ==========================================================

class CropVarietyListView(LoginRequiredMixin, ListView):

    model = CropVariety
    template_name = "crops/variety_list.html"
    context_object_name = "varieties"

    def get_queryset(self):
        return CropVariety.objects.select_related("crop")


class CropVarietyCreateView(LoginRequiredMixin, CreateView):

    model = CropVariety
    form_class = CropVarietyForm
    template_name = "crops/variety_form.html"
    success_url = reverse_lazy("crops:variety_list")

    extra_context = {
        "title": "ثبت رقم جدید",
        "button_text": "ثبت رقم",
    }


class CropVarietyUpdateView(LoginRequiredMixin, UpdateView):

    model = CropVariety
    form_class = CropVarietyForm
    template_name = "crops/variety_form.html"
    success_url = reverse_lazy("crops:variety_list")

    extra_context = {
        "title": "ویرایش رقم",
        "button_text": "ذخیره تغییرات",
    }


class CropVarietyDeleteView(LoginRequiredMixin, DeleteView):

    model = CropVariety
    template_name = "crops/variety_confirm_delete.html"
    success_url = reverse_lazy("crops:variety_list")


# ==========================================================
# CATEGORY
# ==========================================================

class CropCategoryListView(LoginRequiredMixin, ListView):

    model = CropCategory
    template_name = "crops/category_list.html"
    context_object_name = "categories"


class CropCategoryCreateView(LoginRequiredMixin, CreateView):

    model = CropCategory
    form_class = CropCategoryForm
    template_name = "crops/category_form.html"
    success_url = reverse_lazy("crops:category_list")

    extra_context = {
        "title": "ثبت دسته محصول",
        "button_text": "ثبت دسته",
    }


# ==========================================================
# SEASON
# ==========================================================

class SeasonListView(LoginRequiredMixin, ListView):

    model = Season
    template_name = "crops/season_list.html"
    context_object_name = "seasons"


class SeasonCreateView(LoginRequiredMixin, CreateView):

    model = Season
    form_class = SeasonForm
    template_name = "crops/season_form.html"
    success_url = reverse_lazy("crops:season_list")

    extra_context = {
        "title": "ثبت فصل کشت",
        "button_text": "ثبت فصل",
    }


# ==========================================================
# DISEASE
# ==========================================================

class CropDiseaseListView(LoginRequiredMixin, ListView):

    model = CropDisease
    template_name = "crops/disease_list.html"
    context_object_name = "diseases"


class CropDiseaseCreateView(LoginRequiredMixin, CreateView):

    model = CropDisease
    form_class = CropDiseaseForm
    template_name = "crops/disease_form.html"
    success_url = reverse_lazy("crops:disease_list")

    extra_context = {
        "title": "ثبت بیماری",
        "button_text": "ثبت بیماری",
    }