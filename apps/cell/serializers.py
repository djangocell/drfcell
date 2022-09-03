from .models import Cell
from rest_framework import serializers


class CellSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cell
        fields = [field.name for field in Cell._meta.get_fields()]
