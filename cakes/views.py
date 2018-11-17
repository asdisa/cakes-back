from django.shortcuts import render

from rest_framework import generics
from .models import *
from .serializers import *


class ListUnitsView(generics.ListAPIView):
    queryset = Unit.objects.all()
    serializer_class = UnitSerializer

class ListIngredientsView(generics.ListAPIView):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer

class ListImageContainersView(generics.ListAPIView):
    queryset = Image_container.objects.all()
    serializer_class = ImageContainerSerializer
