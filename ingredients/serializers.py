from rest_framework import serializers
from rest_framework.relations import SlugRelatedField
from .models import *
from units.serializers import UnitSerializer
from units.models import Unit

class IngredientSerializer(serializers.ModelSerializer):
    #unit = UnitSerializer()
    unit = serializers.SlugRelatedField(
        slug_field='id',
        queryset=Unit.objects.all()
    )

    class Meta:
        model = Ingredient
        fields = ('id', 'name', 'price_per_gram', 'unit')

