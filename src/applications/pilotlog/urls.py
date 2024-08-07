# Local Folder
# Django Stuff
from django.urls import include, path

# Rest Framework
from rest_framework.routers import DefaultRouter

from .views import AircraftViewSet, FlightViewSet

router = DefaultRouter()
router.register(r"aircrafts", AircraftViewSet)
router.register(r"flights", FlightViewSet)


urlpatterns = [
    path("", include(router.urls)),
]
