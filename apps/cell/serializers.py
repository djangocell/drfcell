from .models import Cell
from rest_framework import serializers


class CellSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cell
        fields = '__all__'
        lookup_field = 'name'
