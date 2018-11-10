from django.shortcuts import render

<<<<<<< HEAD
from rest_framework import generics
from .models import Units
from .serializers import UnitsSerializer


class ListUnitsView(generics.ListAPIView):
    """
    Provides a get method handler.
    """
    queryset = Units.objects.all()
    serializer_class = UnitsSerializer
=======
# Create your views here.
>>>>>>> fcd49909d1fef438d62388e87bef3a9b767b32ca
