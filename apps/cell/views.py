from .models import Cell, Upgrade
from .serializers import CellSerializer, UpgradeSerializer
from rest_framework import generics


class CellList(generics.ListCreateAPIView):
    queryset = Cell.objects.all()
    serializer_class = CellSerializer


class CellDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cell.objects.all()
    serializer_class = CellSerializer


class UpgradeList(generics.ListCreateAPIView):
    queryset = Upgrade.objects.all()
    serializer_class = UpgradeSerializer


class UpgradeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Upgrade.objects.all()
    serializer_class = UpgradeSerializer
