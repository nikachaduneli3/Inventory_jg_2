from rest_framework.routers import DefaultRouter
from .views import SaleOrderViewSet, SaleOrderItemViewSet

router = DefaultRouter(use_regex_path=False)
router.register('orders', SaleOrderViewSet)
router.register('order_items', SaleOrderItemViewSet)

urlpatterns = router.urls
