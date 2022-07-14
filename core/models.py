import pytz
from django.db import models


class EnergyPark(models.Model):
    TIMEZONES = tuple(zip(pytz.all_timezones, pytz.all_timezones))

    ENERGY_TYPE_CHOICES = (
        ("Solar", "Solar"),
        ("Wind", "Wind"),
    )
    name = models.CharField(max_length=50)
    timezone = models.CharField( choices=TIMEZONES, max_length=50)
    energy_type = models.CharField(choices=ENERGY_TYPE_CHOICES, max_length=10)

    def __str__(self):
        return f"{self.name} - {self.energy_type} energy ({self.timezone})"


class Measurement(models.Model):
    energy_park = models.ForeignKey(EnergyPark, on_delete=models.PROTECT, related_name="park")
    timestamp = models.DateTimeField(db_index=True)
    measurement = models.DecimalField(max_digits=25, decimal_places=4, help_text="energy in MW(Mega Watts)")

