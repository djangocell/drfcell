from .models import Monster
from rest_framework import serializers


class MonsterSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Monster
        fields = "__all__".split()
