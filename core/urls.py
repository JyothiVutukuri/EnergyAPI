from django.urls import path, include, re_path
from rest_framework import routers

from core.views import MeasurementsView, EnergyParksView

app_name = "core"

urlpatterns = [
    re_path('measurements/', MeasurementsView.as_view()),
    re_path('energy_parks/', EnergyParksView.as_view()),
]