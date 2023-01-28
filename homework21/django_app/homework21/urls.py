from django.urls import path

from . import views

urlpatterns = [
    path('home/', views.MyView.as_view(), name='index'),
    path('home/index', views.index, name='class-view'), 
    path('home/<data>/', views.MyView.as_view(), name='home')
]
 