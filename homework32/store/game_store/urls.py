from django.urls import path

from . import views


app_name = 'game'
urlpatterns = [
    path('', views.games_all, name='games'),
    path('category/', views.all_categories, name='all_categories'),
    path('sorting/', views.sorting, name='sorting'),
    path('category/<slug:category_slug>/', views.category_games, name='category_games'),
    path('search-games', views.search_games, name='search-games'),
    path('<slug:game_slug>/comment/', views.CommentCreateView.as_view(), name='comment_add'),
    path('comment/<int:pk>/update/', views.CommentUpdateView.as_view(), name='comment_update'),
    path('comment/<int:pk>/delete/', views.CommentDeleteView.as_view(), name='comment_delete'),
    path('<slug:game_slug>/', views.every_game, name='game_slug'),
]