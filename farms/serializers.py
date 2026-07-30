from rest_framework import serializers

from .models import (
    Farm,
    Block,
    Field,
    Crop,
    FieldCrop,
)


class FarmSerializer(serializers.ModelSerializer):
    class Meta:
        model = Farm
        fields = "__all__"


class BlockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Block
        fields = "__all__"


class FieldSerializer(serializers.ModelSerializer):
    class Meta:
        model = Field
        fields = "__all__"


class CropSerializer(serializers.ModelSerializer):
    class Meta:
        model = Crop
        fields = "__all__"


class FieldCropSerializer(serializers.ModelSerializer):
    class Meta:
        model = FieldCrop
        fields = "__all__"