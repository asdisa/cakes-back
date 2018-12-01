from rest_framework import serializers
from .models import *
from ingredients.serializers import UnitSerializer


class ImageContainerSerializer(serializers.ModelSerializer):
    img_medium = serializers.CharField(allow_blank=True)
    img_large = serializers.CharField(allow_blank=True)

    class Meta:
        model = Image_container
        fields = '__all__'


class UsageSerializer(serializers.HyperlinkedModelSerializer):

    id = serializers.ReadOnlyField(source='ingredient.id')
    price_per_gram = serializers.ReadOnlyField(source='ingredient.price_per_gram')
    unit = UnitSerializer(source='ingredient.unit')
    
    class Meta:
        model = Usage

        fields = ("id", "amount_in_units", "price_per_gram", "unit", )



class RecipeSerializer(serializers.ModelSerializer):
    image_container = ImageContainerSerializer(required=False)
    #ingredients = UsageSerializer(source='usage_set', many=True)

    class Meta:
        model = Recipe  
        fields = ("id", "title", "steps", "tags", "image_container")#, "ingredients")


    def create(self, validated_data):
        image_container_data = validated_data.pop('image_container')
        image_container = ImageContainerSerializer.create(ImageContainerSerializer(), validated_data=image_container_data)
            
        recipe, created = Recipe.objects.update_or_create(
            image_container=image_container,
            title=validated_data.pop('title'),
            steps=validated_data.pop('steps'),
            tags=validated_data.pop('tags'))
            
        return recipe


    def update(self, instance, validated_data):
        image_container_data = validated_data.pop('image_container')
        image_container = instance.image_container

        instance.title = validated_data.get('title', instance.title)
        instance.steps = validated_data.get('steps', instance.steps)
        instance.save()

        image_container.img_small = image_container_data.get(
            'img_small',
            image_container.img_small
        )
        image_container.img_medium = image_container_data.get(
            'img_medium',
            image_container.img_medium
        )
        image_container.img_large = image_container_data.get(
            'img_large',
            image_container.img_large
        )
        image_container.save()

        return instance

