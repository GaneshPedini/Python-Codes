from django.shortcuts import render, redirect, HttpResponseRedirect
from store.models.products import Product
from store.models.category import Category
from django.views import View
from store.forms import SingleInventoryForm, BulkInventoryForm

# Create your views here.

class PlaceOrder(View):
    def post(self, request):
        product = request.POST.get('product')
        remove = request.POST.get('remove')
        cart = request.session.get('cart')
        print(f"The product is :{product}")
        if cart:
            quantity = cart.get(product)
            if quantity:
                if remove:
                    if quantity <= 1:
                        cart.pop(product)
                    else:
                        cart[product] = quantity - 1
                else:
                    cart[product] = quantity + 1

            else:
                cart[product] = 1
        else:
            cart = {}
            cart[product] = 1

        request.session['cart'] = cart
        print('cart', request.session['cart'])
        return redirect('order')

    def get(self, request):
        print(f" The Path val : {request.get_full_path()[1:]}")
        return HttpResponseRedirect(f'{request.get_full_path()[1:]}/store_order')


def store_order_all(request):
    products = Product.get_all_products()
    categories = Category.get_all_categories()
    data = dict({})
    data['categories'] = categories
    data['products'] = products
    return render(request, 'order.html', data)

def store_order(request, id):
    cart = request.session.get('cart')
    if not cart:
        request.session['cart'] = {}
    products = None
    categories = Category.get_all_categories()
    #category_id = request.GET.get('category')
    print(f"You have selected {id} category")
    if id:
        print(f"Entering into the category loop!!")
        products = Product.get_all_products_by_categoryid(id)
    else:
        products = Product.get_all_products()
    print(f"Product list: {products}")
    data = dict({})
    data['products'] = products
    data['categories'] = categories

    print('you are : ', request.session.get('email'))
    return render(request, 'order.html', data)

def add_remove_product(request, id):
    print(id)
    product = request.POST.get('product')
    remove = request.POST.get('remove')
    cart = request.session.get('cart')
    print(f"The product is :{product}")
    if cart:
        quantity = cart.get(product)
        if quantity:
            if remove:
                if quantity <= 1:
                    cart.pop(product)
                else:
                    cart[product] = quantity - 1
            else:
                cart[product] = quantity + 1

        else:
            cart[product] = 1
    else:
        cart = {}
        cart[product] = 1

    request.session['cart'] = cart
    print('cart', request.session['cart'])
    products = Product.get_all_products()
    categories = Category.get_all_categories()
    data = dict({})
    data['categories'] = categories
    data['products'] = products
    return render(request, 'order.html', data)


