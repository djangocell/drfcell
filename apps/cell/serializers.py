from .models import Cell
from rest_framework import serializers


class CustomerSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Cell
        fields = "__all__".split()
