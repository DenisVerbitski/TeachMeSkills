from django.urls import path

from . import views

app_name = 'game'
urlpatterns = [
    path('', views.games_all, name='games'),
    path('category/', views.all_categories, name='all_categories'),
    path('sort-alphab/', views.sorting_in_alphabetical_order, name='sort_alphab'),
    path('sort-not-alphab/', views.sorting_not_in_alphabetical_order, name='sort_not_alphab'),
    path('category/<slug:category_slug>/', views.category_games, name='category_games'),
    path('<slug:game_slug>/', views.every_game, name='game_slug'),
]