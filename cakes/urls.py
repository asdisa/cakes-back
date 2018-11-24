from django.urls import path
from .views import *


urlpatterns = [
    path('units/', ListUnitsView.as_view(), name="units"),
    path('ingredients/', ListIngredientsView.as_view(), name="ingredients"),
    path('image_comtainers/', ListImageContainersView.as_view(), name="image_containers"),
    path('recipes/', ListRecipesView.as_view(), name="recipes"),
    path('tags/', ListTagsView.as_view(), name="tags"),
    path('usages/', ListUsagesView.as_view(), name="usages")
]

