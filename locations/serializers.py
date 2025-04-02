from rest_framework import serializers
from .models import Location, ItemLocation
from django.contrib.auth.models import User


class LocationSerializer(serializers.ModelSerializer):
    location_items = serializers.StringRelatedField(many=True)
    manager_name = serializers.StringRelatedField()
    manager = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), write_only=True)
    class Meta:
        model = Location
        fields = '__all__'
