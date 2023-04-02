from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages

from .models import Cart
from game_store.models import Game


def products_in_cart(request):
    carts = Cart.objects.filter(customer=request.user).select_related('product')
    amount = 0
    for cart in carts:
        amount += cart.total_amount()
    return render(request, 'orders/products_in_cart.html', locals())


def cart_add(request, game_slug):
    game = get_object_or_404(Game, slug=game_slug)
    customer = request.user
    cart = Cart.objects.filter(customer=customer, product=game)
    if not cart.exists():
        Cart.objects.create(customer=customer, product=game)
    else:
        cart = cart.first()
        cart.quantity += 1
        cart.save()
    return redirect('orders:products_in_cart')


def cart_remove(request, game_slug):
    game = get_object_or_404(Game, slug=game_slug)
    cart = Cart.objects.filter(customer=request.user, product=game)
    cart.delete()
    return redirect('orders:products_in_cart')


def cart_order(request):
    cart = Cart.objects.filter(customer=request.user)
    messages.success(request, f'Спасибо, ваш заказ сформирован!')
    cart.delete()
    return redirect('game:games')