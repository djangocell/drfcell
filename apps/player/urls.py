from django.urls import path
from .views import PlayerDetail

urlpatterns = [
    path("<str:name>/", PlayerDetail.as_view(), name="player-detail")
]
