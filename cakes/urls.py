from django.urls import path
from .views import *


urlpatterns = [
    path('units/', ListUnitsView.as_view(), name="units"),
    path('image_comtainers/', ListImageContainersView.as_view(), name="image_containers")
]
