from django.urls import path

from . import views

app_name = 'game'
urlpatterns = [
    path('', views.games_all, name='games'),
    path('category/', views.all_categories, name='all_categories'),
    path('<slug:game_slug>/', views.every_game, name='game_slug'),
    path('category/<slug:category_slug>/', views.category_games, name='category_games'),
]