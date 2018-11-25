from django.urls import path
from .views import *


urlpatterns = [
    path('ingredients/', ListIngredientsView.as_view(), name="ingredients")
]