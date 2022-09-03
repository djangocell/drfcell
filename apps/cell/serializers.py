from .models import Cell, Upgrade
from rest_framework import serializers


class CellSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cell
        fields = 'name damage upgrade_resource'.split()


class UpgradeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Upgrade
        fields = [field.name for field in Upgrade._meta.get_fields()]
