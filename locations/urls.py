from django.urls import path
from .views import LocationListCreateApiView, LocationRetrieveUpdateDestroyApiView

urlpatterns = [
        path('', LocationListCreateApiView.as_view()),
        path('<int:pk>/', LocationRetrieveUpdateDestroyApiView.as_view()),
]
