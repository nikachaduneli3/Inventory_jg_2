from django.contrib import admin
from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import PurchaseOrderViewSet, PurchaseOrderItemViewSet

router = DefaultRouter(use_regex_path=False)
router.register('purchase_order', PurchaseOrderViewSet)
router.register('purchase_order_items', PurchaseOrderItemViewSet)

urlpatterns = router.urls
