from rest_framework import generics

import random

from game_store.models import Game
from .serializers import GameSerializer


class GameList(generics.ListAPIView):
    serializer_class = GameSerializer

    def get_queryset(self):
        queryset = Game.objects.all()
        random_games = random.randrange(1, queryset.count() + 1)
        random_params = self.request.query_params.get('random')
        if random_params == 'True':
            return queryset.filter(id=random_games)
        else:
            return queryset