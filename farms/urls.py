from rest_framework.routers import DefaultRouter

from .views import (
    FarmViewSet,
    BlockViewSet,
    FieldViewSet,
    CropViewSet,
    FieldCropViewSet,
)

router = DefaultRouter()

router.register(r"farms", FarmViewSet)
router.register(r"blocks", BlockViewSet)
router.register(r"fields", FieldViewSet)
router.register(r"crops", CropViewSet)
router.register(r"field-crops", FieldCropViewSet)

urlpatterns = router.urls