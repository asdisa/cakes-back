from django.shortcuts import render

from rest_framework import generics
from .models import *
from .serializers import *
from api.auth import *


class ListImageContainersView(generics.ListAPIView):
    queryset = Image_container.objects.all()
    serializer_class = ImageContainerSerializer
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)


class ListRecipesView(generics.ListAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)


class UsageList(generics.ListCreateAPIView):
    queryset = Usage.objects.all()
    serializer_class = UsageSerializer
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)

    def perform_create(self, serializer):
        serializer.save()


class UsageDetailed(generics.RetrieveUpdateDestroyAPIView):
    queryset = Usage.objects.all()
    serializer_class = UsageSerializer
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)


class RecipeList(generics.ListCreateAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)

    def perform_create(self, serializer):
        serializer.save()


class RecipeDetailed(generics.RetrieveUpdateDestroyAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)