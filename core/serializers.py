from rest_framework import serializers
from core.models import Measurement, EnergyPark


class MeasurementSerializer(serializers.ModelSerializer):
    energy_park = serializers.CharField(source='energy_park.name')
    timezone = serializers.CharField(source='energy_park.timezone')
    energy_type = serializers.CharField(source='energy_park.energy_type')

    class Meta:
        model = Measurement
        fields = ("timestamp", "measurement", "energy_park", "timezone", "energy_type")
        read_only_fields = fields


class EnergyParkSerializer(serializers.ModelSerializer):
    class Meta:
        model = EnergyPark
        fields = ("name", "timezone", "energy_type")



