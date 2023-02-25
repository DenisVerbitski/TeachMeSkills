from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.db.models import Avg
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import Game, Category, Comment
from .forms import CommentForm


def games_all(request):
    games = Game.objects.filter(is_active=True).all()
    return render(request, 'games/home.html', {'games': games})


def every_game(request, game_slug):
    game = get_object_or_404(Game, slug=game_slug)
    comments = game.comments.all().order_by('-pub_date')
    average_grade = game.comments.aggregate(Avg('grade'))
    average_grade = average_grade['grade__avg']
    context = {
        'game': game,
        'comments': comments,
        'average_grade': average_grade,
    }
    return render(request, 'games/game.html', context=context)


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

def search_games(request):
    if request.method == 'POST':
        searched = request.POST['searched']
        games = Game.objects.filter(name__icontains=searched)
        return render(request, 'search/search_games.html', {'searched': searched, 'games': games})
    else:
        return render(request, 'search/search_games.html', {})
class CommentCreateView(CreateView):
    template_name = 'forms/comment_create.html'
    form_class = CommentForm

    def form_valid(self, form):
        form.instance.game = Game.objects.get(slug=self.kwargs['game_slug'])
        return super().form_valid(form)
class CommentUpdateView(UpdateView):
    template_name = 'forms/comment_update.html'
    form_class = CommentForm
    queryset = Comment.objects.all()

    def form_valid(self, form):
        return super().form_valid(form)
class CommentDeleteView(DeleteView):
    model = Comment
    template_name = 'forms/comment_delete.html'
    success_url = reverse_lazy('game:games')