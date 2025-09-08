from rest_framework.routers import DefaultRouter
from .viewsets import SuppliersViewSet  # DRF ViewSet

router = DefaultRouter()
router.register(r'', SuppliersViewSet)
urlpatterns = router.urls