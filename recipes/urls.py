from django.urls import path
from .views import *


urlpatterns = [
    path('image_containers/', ListImageContainersView.as_view(), name="image_containers"),
    path('recipes/', ListRecipesView.as_view(), name="recipes"),
    path('tags/', ListTagsView.as_view(), name="tags"),
    path('usages/', ListUsagesView.as_view(), name="usages")
]

