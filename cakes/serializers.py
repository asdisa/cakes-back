from rest_framework import serializers
from .models import *


class UnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Unit
        fields = ("id", "short_name", "full_name", "in_grams")

class ImageContainerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image_container
        fields = ("id", "img_small", "img_medium", "img_large")