from django.shortcuts import render

from rest_framework import generics
from .models import *
from .serializers import *


class ListImageContainersView(generics.ListAPIView):
    queryset = Image_container.objects.all()
    serializer_class = ImageContainerSerializer

class ListTagsView(generics.ListAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class ListUsagesView(generics.ListAPIView):
    queryset = Usage.objects.all()
    serializer_class = UsageSerializer


class ListRecipesView(generics.ListAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
