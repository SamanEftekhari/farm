from django.shortcuts import render

# Create your views here.
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from .forms import CropForm
from .models import Crop


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
            form.save()

            messages.success(
                request,
                "محصول با موفقیت ثبت شد."
            )

            return redirect("crops:crop_list")

    else:
        form = CropForm()

    return render(
        request,
        "crops/crop_form.html",
        {
            "form": form,
            "title": "افزودن محصول",
        },
    )


@login_required
def crop_update(request, pk):

    crop = get_object_or_404(Crop, pk=pk)

    if request.method == "POST":
        form = CropForm(request.POST, instance=crop)

        if form.is_valid():
            form.save()

            messages.success(
                request,
                "محصول با موفقیت ویرایش شد."
            )

            return redirect("crops:crop_list")

    else:
        form = CropForm(instance=crop)

    return render(
        request,
        "crops/crop_form.html",
        {
            "form": form,
            "title": "ویرایش محصول",
        },
    )


@login_required
def crop_delete(request, pk):

    crop = get_object_or_404(Crop, pk=pk)

    if request.method == "POST":
        crop.delete()

        messages.success(
            request,
            "محصول حذف شد."
        )

        return redirect("crops:crop_list")

    return render(
        request,
        "crops/crop_confirm_delete.html",
        {
            "crop": crop,
        },
    )