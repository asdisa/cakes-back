from django.db import models
from units.models import Unit

class Ingredient(models.Model):
    name = models.CharField(max_length=200)
    price_per_gram = models.FloatField()
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name}"
