from django.shortcuts import render

from rest_framework import generics
from .models import *
from .serializers import *


class ListImageContainersView(generics.ListAPIView):
    queryset = Image_container.objects.all()
    serializer_class = ImageContainerSerializer


class ListRecipesView(generics.ListAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer


class UsageList(generics.ListCreateAPIView):
    queryset = Usage.objects.all()
    serializer_class = UsageSerializer

    def perform_create(self, serializer):
        serializer.save()


class UsageDetailed(generics.RetrieveUpdateDestroyAPIView):
    queryset = Usage.objects.all()
    serializer_class = UsageSerializer


class RecipeList(generics.ListCreateAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer

    def perform_create(self, serializer):
        serializer.save()


class RecipeDetailed(generics.RetrieveUpdateDestroyAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer