from .models import Monster
from rest_framework import serializers


class MonsterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Monster
        fields = '__all__'
        lookup_field = 'name'
