import datetime

from django.utils import timezone
from import_export import resources
from import_export.fields import Field
from import_export.widgets import ForeignKeyWidget

from core.models import EnergyPark, Measurement


class EnergyParkResource(resources.ModelResource):
    name = Field(attribute='name', column_name='park_name')
    timezone = Field(attribute='timezone')
    energy_type = Field(attribute='energy_type')

    class Meta:
        model = EnergyPark


class MeasurementResource(resources.ModelResource):
    energy_park = Field(
        column_name='energy_park_id',
        attribute='energy_park',
        widget=ForeignKeyWidget(EnergyPark, 'id'))
    timestamp = Field(attribute='timestamp', column_name='datetime')
    measurement = Field(attribute='measurement', column_name='MW')

    class Meta:
        model = Measurement

    def __init__(self, request=None):
        self.request = request
        super().__init__()

    def before_import_row(self, row, row_number=None, **kwargs):
        energy_park = self.request.POST.get('energy_park', None)
        if energy_park:
            self.request.session['context'] = energy_park
        else:
            try:
                energy_park = self.request.session['context']
            except KeyError as e:
                raise Exception("Energy park context failure on row import, " +
                                f"check resources.py for more info: {e}")
        row['energy_park_id'] = energy_park

    # def before_import(self, dataset, using_transactions, dry_run, **kwargs):
    #     energy_park = self.request.POST.get('energy_park', None)
    #     if energy_park:
    #         self.request.session['context'] = energy_park
    #     else:
    #         try:
    #             energy_park = self.request.session['context']
    #         except KeyError as e:
    #             raise Exception("Energy park context failure on row import, " +
    #                             f"check resources.py for more info: {e}")
    #     if 'energy_park_id' not in dataset.headers:
    #         dataset.insert_col(0, lambda row: energy_park, header='energy_park_id')





