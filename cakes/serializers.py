from rest_framework import serializers
from .models import Units


class UnitsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Units
        fields = ("id", "short_name", "full_name", "in_grams")