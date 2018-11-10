from django.urls import path
from .views import ListUnitsView


urlpatterns = [
    path('units/', ListUnitsView.as_view(), name="units")
]
