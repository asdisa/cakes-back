from django.db import models

<<<<<<< HEAD
class Units(models.Model):
    # short and universal title
    short_name = models.CharField(max_length=20)
    # long title with specified ingredient
    full_name = models.CharField(max_length=255, null=True)
    # weight in gramms
    in_grams = models.FloatField(default=1.0)    

    def __str__(self):
        return "{} - {}".format(self.short_name, str(self.in_gramms))
=======
# Create your models here.
>>>>>>> fcd49909d1fef438d62388e87bef3a9b767b32ca
