from rest_framework import serializers
from .models import *
from ingredients.serializers import UnitSerializer


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
    price_per_gram = serializers.ReadOnlyField(source='ingredient.price_per_gram')
    unit = UnitSerializer(source='ingredient.unit')
    
    class Meta:
        model = Usage

        fields = ("id", "price_per_gram", "unit", )



class RecipeSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True)
    image_container = ImageContainerSerializer()
    ingredients = UsageSerializer(source='usage_set', many=True)

    class Meta:
        model = Recipe  

        fields = ("id", "title", "steps", "tags", "ingredients", "image_container")



