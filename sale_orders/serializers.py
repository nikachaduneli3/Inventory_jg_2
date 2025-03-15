from rest_framework import serializers
from .models import SaleOrder, SaleOrderItem
from products.models import Item

class SaleOrderItemSerializer(serializers.ModelSerializer):
    sale_order_display = serializers.StringRelatedField(source='sale_order', read_only=True)
    sale_order = serializers.PrimaryKeyRelatedField(queryset=SaleOrder.objects.all(), write_only=True)
    item_name = serializers.StringRelatedField(source='item', read_only=True)
    item = serializers.PrimaryKeyRelatedField(queryset=Item.objects.all(), write_only=True)

    class Meta:
        model = SaleOrderItem
        fields = '__all__'

class SaleOrderSerializer(serializers.ModelSerializer):
    sale_items = SaleOrderItemSerializer(many=True, read_only=True)
    class Meta:
        model = SaleOrder
        fields = '__all__'

