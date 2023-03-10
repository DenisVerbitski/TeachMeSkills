from rest_framework import generics, filters

import random

from game_store.models import Game
from .serializers import GameSerializer


class GameList(generics.ListAPIView):
    serializer_class = GameSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['name', 'price', 'release_date']

    def get_queryset(self):
        queryset = Game.objects.all().order_by('id')
        random_games = random.randrange(1,  queryset.count() + 1)
        random_params = self.request.query_params.get('random')
        if random_params == 'True':
            return queryset.filter(id=random_games)
        else:
            return queryset