from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AircraftViewSet

router = DefaultRouter()
router.register(r'aircrafts', AircraftViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
