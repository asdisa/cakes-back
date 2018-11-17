from django.db import models

class Unit(models.Model):
    # short and universal title
    short_name = models.CharField(max_length=20)
    # long title with specified ingredient
    full_name = models.CharField(max_length=255, null=True)
    # weight in gramms
    in_grams = models.FloatField(default=1.0)    

    def __str__(self):
        return "{} - {}".format(self.short_name, str(self.in_gramms))


class Image_container(models.Model):
    img_small = models.CharField(max_length=500)
    img_medium = models.CharField(max_length=500)
    img_large = models.CharField(max_length=500)

    def __str__(self):
        return img_small
