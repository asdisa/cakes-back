from django.urls import path
from .views import *

urlpatterns = [
    path('units/', ListUnitsView.as_view(), name="units"),
]