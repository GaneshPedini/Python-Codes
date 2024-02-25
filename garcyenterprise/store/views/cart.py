from django.shortcuts import render, redirect
from django.contrib.auth.hashers import check_password
from django.views import View
from store.models.products import Product

def cart_view(request):
    print(f"The cart in the cart view is: {request.session['cart']}")
    ids = list(request.session.get('cart').keys())
    products = Product.get_products_by_id(ids)
    print(products)
    return render(request, 'cart.html', {'products': products})

