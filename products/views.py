from rest_framework import viewsets
from .serializers import ItemSerializer, CategorySerializer
from .models import Item, Category
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    permission_classes = [IsAuthenticated]

    def list(self, *args, **kwargs):
        return super().list(*args, **kwargs)



class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

import requests
