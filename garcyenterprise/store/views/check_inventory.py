from django.shortcuts import render, redirect, HttpResponseRedirect
from store.models.products import Product
from store.models.category import Category
from django.views import View


# Create your views here.
class CheckInventory(View):

    def post(self, request):
        return redirect('view_inventory')

    def get(self, request):
        print(f" The Path val : {request.get_full_path()[1:]}")
        return HttpResponseRedirect(f'/store_inventory{request.get_full_path()[1:]}')


def store_inventory(request):

    products = None
    categories = Category.get_all_categories()
    category_id = request.GET.get('category')
    print(f"You have selected {category_id} category")
    if category_id:
        print(f"Entering into the category loop!!")
        products = Product.get_all_products_by_categoryid(category_id)
    else:
        products = Product.get_all_products()
    print(f"Product list: {products}")
    data = dict({})
    data['products'] = products
    data['categories'] = categories

    print('you are : ', request.session.get('email'))
    return render(request, 'view_inventory.html', data)