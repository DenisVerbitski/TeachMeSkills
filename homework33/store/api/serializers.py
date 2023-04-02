from rest_framework import serializers

from game_store.models import Game, Category


class GameSerializer(serializers.ModelSerializer):
    category = serializers.ReadOnlyField(source='category.name')

    class Meta:
        model = Game
        fields = (
            'id', 
            'name', 
            'description', 
            'release_date',
            'price', 
            'slug', 
            'category'
            )


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = (
            'id', 
            'name', 
            'description', 
            'slug', 
            'games_amount')