from rest_framework.routers import DefaultRouter
from .viewsets import ProductsViewSet  # DRF ViewSet

router = DefaultRouter()
router.register(r'', ProductsViewSet)
urlpatterns = router.urls