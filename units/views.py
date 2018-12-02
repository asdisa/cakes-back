from django.shortcuts import render

from rest_framework import generics
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import AllowAny
from .models import *
from .serializers import *


class CsrfExemptSessionAuthentication(SessionAuthentication):
    def enforce_csrf(self, request):
        return None


class UnitList(generics.ListCreateAPIView):
    queryset = Unit.objects.all()
    serializer_class = UnitSerializer
    permission_classes = (AllowAny, )
    authentication_classes = (CsrfExemptSessionAuthentication,)


    def perform_create(self, serializer):
        serializer.save()


class UnitDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Unit.objects.all()
    serializer_class = UnitSerializer
    permission_classes = (AllowAny, )
    authentication_classes = (CsrfExemptSessionAuthentication,)


