from django.urls import path

from . import views


app_name = 'orders'
urlpatterns = [
    path('list/', views.products_in_cart, name='products_in_cart'),
    path('add/<slug:game_slug>/', views.cart_add, name='cart_add'),
    path('remove/<slug:game_slug>', views.cart_remove, name="cart_remove"),
    path('order/', views.cart_order, name="cart_order"),
]