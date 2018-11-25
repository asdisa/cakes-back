from rest_framework import serializers
from .models import *


class UnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Unit
        fields = ("id", "short_name", "full_name", "weight_in_grams")
