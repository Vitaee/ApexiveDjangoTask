# Local Folder
# Local Folder
from .models import Flight, Aircraft
from .serializers import FlightSerializer, AircraftSerializer

# Rest Framework
from rest_framework import viewsets


class AircraftViewSet(viewsets.ModelViewSet):
    queryset = Aircraft.objects.all()
    serializer_class = AircraftSerializer


class FlightViewSet(viewsets.ModelViewSet):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer
