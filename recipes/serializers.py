from rest_framework import serializers
from .models import *
from ingredients.serializers import IngredientSerializer
from drf_writable_nested import WritableNestedModelSerializer

class ImageContainerSerializer(serializers.ModelSerializer):
    img_medium = serializers.CharField(allow_blank=True)
    img_large = serializers.CharField(allow_blank=True)

    class Meta:
        model = Image_container
        fields = '__all__'


class UsageSerializer(WritableNestedModelSerializer):
    ingredient = IngredientSerializer()
    
    class Meta:
        model = Usage
        fields = ("ingredient", "amount_in_units")
        extra_kwargs = {
            'recipe_id': {
                'validators': []
            }
        }

    '''    
    def create(self, validated_data):
        ingredient_data = validated_data.pop('ingredient')
        ingredient = IngredientSerializer.create(IngredientSerializer(), validated_data=ingredient_data)
        
        usage, created = Usage.objects.update_or_create(
            ingredient=ingredient,
            amount_in_units=validated_data.pop('amount_in_units'))
            
        return usage
        '''



class RecipeSerializer(WritableNestedModelSerializer):
    image_container = ImageContainerSerializer(required=False)
    ingredients = UsageSerializer(source='usage_set', many=True)
    
    class Meta:
        model = Recipe  
        fields = ("id", "title", "steps", "tags", "image_container", "ingredients")

    '''
    def create(self, validated_data):
        image_container_data = validated_data.pop('image_container')
        image_container = ImageContainerSerializer.create(ImageContainerSerializer(), validated_data=image_container_data)
        
        ingredients_data = validated_data.pop('usage_set')
        ingredients = [UsageSerializer.create(UsageSerializer(partial=True), validated_data=ingredient_data) for ingredient_data in ingredients_data]
        print(f'\n\n\n{ingredients}\n\n\n')
        recipe, created = Recipe.objects.update_or_create(
            ingredients=ingredients,
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
'''

