from django.http import Http404
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator

from .models import Game, Category


def games_all(request):
    games = Game.objects.filter(is_active=True).all()
    return render(request, 'games/home.html', {'games': games})


def every_game(request, game_slug):
    game = Game.objects.get(slug=game_slug)
    if game is not None:
        return render(request, 'games/game.html', {'game': game})
    else:
        raise Http404('Упс кажется такой игры нет!')


def all_categories(request):
    categories = Category.objects.filter(is_active=True)
    return render(request, 'category/all_categories.html', {'categories': categories})


def category_games(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    games = category.game_set.filter(is_active=True).all()
    context = {
        'category': category,
        'games': games
    }
    return render(request, 'category/category_games.html', context)


def sorting_in_alphabetical_order(request):
    sorted_games = Game.objects.order_by('name').all()
    paginator = Paginator(sorted_games, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'sorting/sort_alphab.html', {'page_obj': page_obj})


def sorting_not_in_alphabetical_order(request):
    sorted_games = Game.objects.order_by('-name').all()
    paginator = Paginator(sorted_games, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'sorting/sort_alphab.html', {'page_obj': page_obj})