from django.shortcuts import render, redirect, HttpResponseRedirect
from store.models.products import Product
from store.models.category import Category
from django.views import View
from store.forms import SingleInventoryForm, BulkInventoryForm

# Create your views here.

class PlaceOrder(View):
    def post(self, request):
        return redirect('place_order')

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
