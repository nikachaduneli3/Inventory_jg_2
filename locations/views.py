from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import LocationSerializer
from .models import Location


class LocationListCreateApiView(ListCreateAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer


class LocationRetrieveUpdateDestroyApiView(RetrieveUpdateDestroyAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer

