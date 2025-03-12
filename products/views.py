from rest_framework import viewsets
from .serializers import ItemSerializer, CategorySerializer
from .models import Item, Category


class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

    def get_queryset(self):
        return super().get_queryset().filter(archived=False)

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
