from rest_framework import serializers
from .models import Location, ItemLocation
from django.contrib.auth.models import User

class LocationItemSerializer(serializers.ModelSerializer):
    item = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = ItemLocation
        fields = ['id', 'item', 'qty']

class LocationSerializer(serializers.ModelSerializer):
    location_items = LocationItemSerializer(many=True)
    manager_name = serializers.StringRelatedField(read_only=True, source='manager')
    manager = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), write_only=True)
    class Meta:
        model = Location
        fields = ['id', 'name',  'location_items', 'manager', 'manager_name']
