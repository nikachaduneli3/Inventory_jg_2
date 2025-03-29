from rest_framework.viewsets import ModelViewSet
from .serializers import PurchaseOrderSerializer, PurchaseOrderItemSerializer
from .models import PurchaseOrder, PurchaseOrderItem
from rest_framework.decorators import action, permission_classes
from  rest_framework.response import Response
from locations.models import ItemLocation


class PurchaseOrderViewSet(ModelViewSet):
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer

    @action(detail=True, methods=['post'])
    def validate(self, request, pk):
        purchase_order = PurchaseOrder.objects.get(pk=pk)
        if purchase_order.completed:
            return Response({'message': 'Purchase Order is already validated.'})
        location = purchase_order.location

        for purchase_item in purchase_order.purchase_items.all():
            item = purchase_item.item
            qty = purchase_item.quantity
            location_item, created = ItemLocation.objects.get_or_create(item=item, location=location)
            if created:
                location_item.qty = qty
            else:
                location_item.qty += qty

            location_item.save()

        purchase_order.completed = True
        purchase_order.save()
        return  Response({'message': 'Order has been completed'})


class PurchaseOrderItemViewSet(ModelViewSet):
    queryset = PurchaseOrderItem.objects.all()
    serializer_class = PurchaseOrderItemSerializer



