from django.urls import path
from .views import MonsterList, MonsterDetail

urlpatterns = [
    path("", MonsterList.as_view(), name="monster-list"),
    path("<str:name>/", MonsterDetail.as_view(), name="monster-detail")
]
