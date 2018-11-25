from django.db import models


class Unit(models.Model):
    short_name = models.CharField(max_length=20)
    full_name = models.CharField(max_length=255, null=True)
    weight_in_grams = models.FloatField(default=1.0)    

    def __str__(self):
        return f"{self.short_name}"


class Ingredient(models.Model):
    name = models.CharField(max_length=200)
    price_per_gram = models.FloatField()
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name}"
