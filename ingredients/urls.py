from django.urls import path
from .views import *


urlpatterns = [
    path('ingredients/', IngredientList.as_view(), name="ingredient-list"),
    path('ingredients/<int:pk>', IngredientDetail.as_view(), name="ingredient-detailed"),
]
