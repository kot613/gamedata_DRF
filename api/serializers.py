from rest_framework import serializers
from .models import Game


class GameSerializer(serializers.ModelSerializer):
    """
    Serializer for Model Game
    """
    class Meta:
        model = Game
        fields = '__all__'


class GlobalSalesUpdateSerializer(serializers.ModelSerializer):
    """
        Serializer for update global_sale in model Game
    """
    class Meta:
        model = Game
        fields = '__all__'
        read_only_fields = ['name', 'platform', 'year', 'genre']



