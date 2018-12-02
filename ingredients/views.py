from django.shortcuts import render

from rest_framework import generics
from rest_framework.response import Response
from rest_framework.reverse import reverse
from .models import *
from .serializers import *


class IngredientList(generics.ListCreateAPIView):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer

    def perform_create(self, serializer):
        serializer.save()


class IngredientDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer
