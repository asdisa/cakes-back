from django.urls import path
from .views import *


urlpatterns = [
    path('image_containers/', ListImageContainersView.as_view(), name="image_containers"),
    #path('recipes/', ListRecipesView.as_view(), name="recipes"),
    path('usages/', UsageList.as_view(), name="usages"),
    path('recipes/', RecipeList.as_view(), name="usage-list"),
    path('recipes/<int:pk>', RecipeDetailed.as_view(), name="usage-detailed"),

]

