from django.urls import path
from .views import CellList, CellDetail, UpgradeList, UpgradeDetail

urlpatterns = [
    path("", CellList.as_view(), name="cell-list"),
    path("upgrade/", UpgradeList.as_view(), name="cell-upgrade-list"),
    path("<str:pk>/", CellDetail.as_view(), name="cell-detail"),
    path("upgrade/<str:pk>/", UpgradeDetail.as_view(), name="cell-upgrade-detail")
]
