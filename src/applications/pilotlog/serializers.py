# Local Folder
# Rest Framework
from rest_framework import serializers

from .models import Aircraft, Flight


class AircraftSerializer(serializers.ModelSerializer):
    extra_info = serializers.SerializerMethodField()

    class Meta:
        model = Aircraft
        fields = [
            "user_id",
            "guid",
            "make",
            "model",
            "reference",
            "modified",
            "extra_info",
        ]

    def get_extra_info(self, obj):
        return f"{obj.make} {obj.model}"


class FlightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flight
        fields = "__all__"
