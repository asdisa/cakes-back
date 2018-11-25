from django.urls import path
from .views import *
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('units/', UnitList.as_view(), name="unit-list"),
    path('units/<int:pk>', UnitDetail.as_view(), name="units-detailed"),
]

urlpatterns = format_suffix_patterns(urlpatterns)