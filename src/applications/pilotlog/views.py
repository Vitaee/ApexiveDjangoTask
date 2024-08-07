from rest_framework import viewsets
from .models import Aircraft
from .serializers import AircraftSerializer

class AircraftViewSet(viewsets.ModelViewSet):
    queryset = Aircraft.objects.all()
    serializer_class = AircraftSerializer