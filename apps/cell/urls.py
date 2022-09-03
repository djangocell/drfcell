from django.urls import path
from .views import CellList, CellDetail

urlpatterns = [
    path("", CellList.as_view(), name="cell-list"),
    path("<str:name>/", CellDetail.as_view(), name="cell-detail")
]
