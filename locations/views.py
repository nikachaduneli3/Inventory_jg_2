from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import LocationSerializer
from .models import Location
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_cookie
from django.core.cache import cache
from django.contrib.auth.models import  User, AnonymousUser

class LocationListCreateApiView(ListCreateAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        user = self.request.user
        cache_key = f'locations_{user.id}'
        if user.id:
            if cache.get(cache_key): return cache.get(cache_key)
        if not user.is_superuser:
            queryset = queryset.filter(manager_id=self.request.user.id)
        cache.set(cache_key, queryset, 100)
        return queryset


class LocationRetrieveUpdateDestroyApiView(RetrieveUpdateDestroyAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer

