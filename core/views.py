from django.shortcuts import render

# Create your views here.
from rest_framework import permissions, generics, status, exceptions

from core.models import Measurement, EnergyPark
from core.serializers import MeasurementSerializer, EnergyParkSerializer


class MeasurementsView(generics.ListAPIView):
    """
    API endpoint that gives list of measurements by filtering the required parameters.
    """
    serializer_class = MeasurementSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        """
        Optionally restricts the returned purchases to a given user,
        by filtering against query parameters in the URL.
        """
        queryset = Measurement.objects.all()
        park_names = self.request.query_params.get('park_names')
        from_timestamp = self.request.query_params.get('from_timestamp')
        to_timestamp = self.request.query_params.get('to_timestamp')
        energy_type = self.request.query_params.get('energy_type')
        if park_names:
            queryset = queryset.filter(energy_park__name__in=park_names.split(","))
        else:
            raise exceptions.ParseError(f"Need to specify which park(s) information you need ")
        if from_timestamp:
            queryset = queryset.filter(timestamp__gte=from_timestamp)
        if to_timestamp:
            queryset = queryset.filter(timestamp__lte=to_timestamp)
        if energy_type:
            queryset = queryset.filter(energy_park__energy_type=energy_type)

        return queryset


class EnergyParksView(generics.ListAPIView):
    """
    API endpoint that gives list of energy parks.
    """

    queryset = EnergyPark.objects.all()
    serializer_class = EnergyParkSerializer
    permission_classes = [permissions.IsAuthenticated]





