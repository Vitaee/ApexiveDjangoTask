# Local Folder
# Local Folder
# Rest Framework
from rest_framework import viewsets

from .models import Aircraft, Flight
from .serializers import AircraftSerializer, FlightSerializer


class AircraftViewSet(viewsets.ModelViewSet):
    queryset = Aircraft.objects.all()
    serializer_class = AircraftSerializer


class FlightViewSet(viewsets.ModelViewSet):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer
