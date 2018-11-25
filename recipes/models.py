from django.db import models
from ingredients.models import Ingredient
from django.contrib.postgres.fields import ArrayField


class Image_container(models.Model):
    img_small = models.CharField(max_length=500)
    img_medium = models.CharField(max_length=500, null=True)
    img_large = models.CharField(max_length=500, null=True)

    def __str__(self):
        return self.img_small


class Tag(models.Model):
    text = models.CharField(max_length=50)

    def __str__(self):
        return f"#{self.text}"


class Recipe(models.Model):
    title = models.CharField(max_length=500)
    steps = ArrayField(models.TextField())
    ingredients = models.ManyToManyField(Ingredient, through='Usage',)
    tags = models.ManyToManyField(Tag)
    image_container = models.ForeignKey(Image_container, on_delete=models.CASCADE)

    def __str__(self):
        return f"#{self.title}"

    class Meta:
        ordering = ('title',)


class Usage(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    amount_in_units = models.FloatField()