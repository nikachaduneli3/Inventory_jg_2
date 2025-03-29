from rest_framework import serializers
from .models import Location, ItemLocation

class LocationSerializer(serializers.ModelSerializer):
    location_items = serializers.StringRelatedField(many=True)
    manager = serializers.StringRelatedField()
    class Meta:
        model = Location
        fields = '__all__'
