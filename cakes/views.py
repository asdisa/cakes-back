from django.shortcuts import render

from rest_framework import generics
from .models import Units
from .serializers import UnitsSerializer


class ListUnitsView(generics.ListAPIView):
    """
    Provides a get method handler.
    """
    queryset = Units.objects.all()
    serializer_class = UnitsSerializer
