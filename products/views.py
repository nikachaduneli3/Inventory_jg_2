from rest_framework import viewsets
from .serializers import ItemSerializer, CategorySerializer
from .models import Item, Category
from rest_framework.permissions import IsAuthenticated
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page


class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    permission_classes = [IsAuthenticated]

    @method_decorator(cache_page(5))
    def list(self, *args, **kwargs):
        print('olalallalal')
        return super().list(*args, **kwargs)



class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

import requests
