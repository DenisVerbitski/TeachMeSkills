
from django.shortcuts import render, get_object_or_404
from .models import Game, Category


def every_game(request, game_slug):
    game = get_object_or_404(Game, slug=game_slug)
    return render(request, 'games/game.html', {'game': game})


def games_all(request):
    games = Game.objects.filter(is_active=True).all()
    return render(request, 'games/home.html', {'games': games})


def category_games(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    games = Game.objects.filter(is_active=True, category=category)
    context = {
        'category': category,
        'games': games
    }
    return render(request, 'category/category_games.html', context)


def all_categories(request):
    categories = Category.objects.filter(is_active=True)
    return render(request, 'category/all_categories.html', {'categories': categories})