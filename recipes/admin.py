from django.contrib import admin
from .models import *

admin.site.register(Image_container)
admin.site.register(Tag)
admin.site.register(Recipe)
admin.site.register(Usage)