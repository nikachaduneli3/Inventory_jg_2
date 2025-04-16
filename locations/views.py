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
        user = self.request.user
        queryset = cache.get(f'locations_{user.id}')
        if queryset:
            return queryset
        if user.is_superuser:
            queryset = self.queryset.all()
        elif user.id:
            queryset = self.queryset.filter(manager=user)
        else:
            return self.queryset.filter(manager=False)

        cache.set(f'locations_{user.id}', queryset, 70)
        return queryset


class LocationRetrieveUpdateDestroyApiView(RetrieveUpdateDestroyAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer

