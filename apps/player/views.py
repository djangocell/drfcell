from .models import Player
from .serializers import PlayerSerializer
from rest_framework import generics


class PlayerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer
