from django.db import models
from django.contrib.postgres.fields import ArrayField

class Unit(models.Model):
    short_name = models.CharField(max_length=20)
    full_name = models.CharField(max_length=255, null=True)
    weight_in_grams = models.FloatField(default=1.0)    

    def __str__(self):
        return f"{self.short_name}"


class Ingredient(models.Model):
    name = models.CharField(max_length=200)
    price_per_unit = models.FloatField()
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name}"


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