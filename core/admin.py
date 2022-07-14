from django.contrib import admin

from core.forms import MeasurementImportForm
from core.models import EnergyPark, Measurement
from import_export.admin import ImportMixin
from import_export.formats import base_formats

from core.resources import EnergyParkResource, MeasurementResource


@admin.register(EnergyPark)
class EnergyParkAdmin(ImportMixin, admin.ModelAdmin):
    list_display = ["id", "name", "timezone", "energy_type"]
    search_fields = ["name"]

    list_filter = ["name", "timezone", "energy_type"]

    resource_class = EnergyParkResource
    formats = (base_formats.CSV, )


@admin.register(Measurement)
class MeasurementAdmin(ImportMixin, admin.ModelAdmin):
    list_display = ["timestamp", "measurement", "energy_park"]
    search_fields = ["energy_park"]
    list_filter = ["energy_park"]

    resource_class = MeasurementResource
    formats = (base_formats.CSV, )

    def get_import_form(self):
        return MeasurementImportForm

    def get_import_resource_kwargs(self, request, *args, **kwargs):
        resource_kwargs = super().get_resource_kwargs(request, *args, **kwargs)
        resource_kwargs['request'] = request
        return resource_kwargs




