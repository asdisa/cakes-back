from django.shortcuts import render

from rest_framework import generics
from .models import *
from .serializers import *


class ListUnitsView(generics.ListAPIView):
    queryset = Unit.objects.all()
    serializer_class = UnitSerializer
