from django.shortcuts import render, get_object_or_404
from django.db.models import Avg
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

import datetime   

from .models import Game, Category, Comment
from .forms import CommentForm


def games_all(request):
    games = Game.objects.filter(is_active=True).all()
    return render(request, 'games/home.html', {'games': games})


@login_required(login_url='user:login')
def every_game(request, game_slug):
    game = get_object_or_404(Game, slug=game_slug)
    comments = game.comments.all().order_by('-pub_date')
    last = request.COOKIES.get(game_slug)
    average_grade = game.comments.aggregate(Avg('grade'))
    session_key = f'{game_slug}_visits'
    visits = request.session.get(session_key, 0)
    visits += 1
    request.session[session_key] = visits
    context = {
        'game': game,
        'comments': comments,
        'last': last,
        'visits': visits,
        'average_grade': average_grade['grade__avg'],
    }
    response = render(request, 'games/game.html', context=context)
    visit_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    response.set_cookie(game_slug, visit_time)
    return response


def all_categories(request):
    categories = Category.objects.filter(is_active=True)
    return render(request, 'category/all_categories.html', {'categories': categories})


@login_required(login_url='user:login')
def category_games(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    games = category.game_set.filter(is_active=True, category=category)
    context = {
        'category': category,
        'games': games
    }
    return render(request, 'category/category_games.html', context)


def sorting(request):
    sort = request.GET.get('sort')  
    sort_order = {
        'name_desc': Game.objects.order_by('-name'),
        'name_asc': Game.objects.order_by('name'),
    }
    games = sort_order.get(sort)
    return render(request, 'sorting/sorting.html', {'games': games})


def search_games(request):
    if request.method == 'POST':
        searched = request.POST['searched']
        games = Game.objects.filter(name__icontains=searched)
        return render(request, 'search/search_games.html', {'searched': searched, 'games': games})
    else:
        return render(request, 'search/search_games.html', {})


class CommentCreateView(CreateView, LoginRequiredMixin):
    template_name = 'comments/comment_create.html'
    form_class = CommentForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.game = Game.objects.get(slug=self.kwargs['game_slug'])
        return super().form_valid(form)


class CommentUpdateView(UpdateView):
    model = Comment
    template_name = 'comments/comment_update.html'
    form_class = CommentForm


class CommentDeleteView(DeleteView):
    model = Comment
    template_name = 'comments/comment_delete.html'
    success_url = reverse_lazy('game:games')