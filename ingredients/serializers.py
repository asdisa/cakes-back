from rest_framework import serializers
from .models import *
from units.serializers import UnitSerializer

class IngredientSerializer(serializers.ModelSerializer):
    unit = UnitSerializer()
    
    class Meta:
        model = Ingredient
        fields = ("id", "price_per_gram", "unit")