from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from .models import (
    Farm,
    Block,
    Field,
    Crop,
    FieldCrop,
)

from .serializers import (
    FarmSerializer,
    BlockSerializer,
    FieldSerializer,
    CropSerializer,
    FieldCropSerializer,
)


class FarmViewSet(viewsets.ModelViewSet):
    queryset = Farm.objects.all()
    serializer_class = FarmSerializer


class BlockViewSet(viewsets.ModelViewSet):
    queryset = Block.objects.all()
    serializer_class = BlockSerializer


class FieldViewSet(viewsets.ModelViewSet):
    queryset = Field.objects.all()
    serializer_class = FieldSerializer


class CropViewSet(viewsets.ModelViewSet):
    queryset = Crop.objects.all()
    serializer_class = CropSerializer


class FieldCropViewSet(viewsets.ModelViewSet):
    queryset = FieldCrop.objects.all()
    serializer_class = FieldCropSerializer