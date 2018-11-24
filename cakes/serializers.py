from rest_framework import serializers
from .models import *


class UnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Unit
        fields = ("id", "short_name", "full_name", "weight_in_grams")

class IngredientSerializer(serializers.ModelSerializer):
    unit = UnitSerializer()
    
    class Meta:
        model = Ingredient
        fields = ("id", "price_per_unit", "unit")

class ImageContainerSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = Image_container
        fields = ("id", "img_small", "img_medium", "img_large")


class TagSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tag
        fields = ("id", "text")


class UsageSerializer(serializers.HyperlinkedModelSerializer):

    id = serializers.ReadOnlyField(source='ingredient.id')
    name = serializers.ReadOnlyField(source='ingredient.name')
    price_per_unit = serializers.ReadOnlyField(source='price_per_unit.name')


    class Meta:
        model = Usage

        fields = ('id', 'name', 'price_per_unit', 'amount_in_units', )



class RecipeSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True)
    image_container = ImageContainerSerializer()

    class Meta:
        model = Recipe  

        fields = ("id", "title", "steps", "tags", "image_container")



