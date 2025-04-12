from rest_framework.viewsets import ModelViewSet
from .serializers import SaleOrderSerializer, SaleOrderItemSerializer, ListSaleOrderItemSerializer
from .models import SaleOrder, SaleOrderItem
from rest_framework.decorators import action, permission_classes
from  rest_framework.response import Response
from locations.models import Location, ItemLocation
from rest_framework.permissions import BasePermission
from .models import SaleOrder

class MangerCanValidate(BasePermission):
    message = 'არ ხარ მენეჯერი ჯიგო !'

    def has_permission(self, request, view):
        id = view.kwargs.get('pk')
        obj = SaleOrder.objects.get(id=id)
        return request.user == obj.location.manager


class SaleOrderViewSet(ModelViewSet):
    queryset = SaleOrder.objects.all()
    serializer_class = SaleOrderSerializer

    @action(detail=True, methods=['post'], permission_classes=[MangerCanValidate])
    def validate(self, request, pk):
        sale_order = SaleOrder.objects.get(pk=pk)
        location = sale_order.location

        if sale_order.completed:
            return Response({'message': 'Sale Order is already validated.'})

        for sale_item in sale_order.sale_items.all():
            item = sale_item.item

            location_item, created = ItemLocation.objects.get_or_create(item=item, location=location)

            if location_item.qty >= sale_item.qty:
                location_item.qty -= sale_item.qty
                location_item.save()
            else: return Response({'message': 'არალი საკმარისი რაოდენობა'})

        sale_order.completed = True
        sale_order.save()
        return  Response({'message': 'Order has been completed'})


class SaleOrderItemViewSet(ModelViewSet):
    queryset = SaleOrderItem.objects.all()
    serializer_class = SaleOrderItemSerializer

    def get_serializer_class(self):
        if self.action == 'list':
            return ListSaleOrderItemSerializer
        return self.serializer_class