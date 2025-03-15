from rest_framework import serializers
from .models import PurchaseOrder, PurchaseOrderItem
from products.models import Item


class PurchaseOrderItemSerializer(serializers.ModelSerializer):
    purchase_order_display = serializers.StringRelatedField(source='purchase_order', read_only=True)
    purchase_order = serializers.PrimaryKeyRelatedField(queryset=PurchaseOrder.objects.all(), write_only=True)

    item_name = serializers.StringRelatedField(source='item', read_only=True)
    item = serializers.PrimaryKeyRelatedField(queryset=Item.objects.all(), write_only=True)

    class Meta:
        model = PurchaseOrderItem
        fields = '__all__'


class PurchaseOrderSerializer(serializers.ModelSerializer):
    purchase_items = PurchaseOrderItemSerializer(many=True, read_only=True)
    class Meta:
        model = PurchaseOrder
        fields = '__all__'

