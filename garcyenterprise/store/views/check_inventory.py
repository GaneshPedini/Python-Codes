from django.shortcuts import render, redirect, HttpResponseRedirect
from store.models.products import Product
from store.models.category import Category
from django.views import View


# Create your views here.
class CheckInventory(View):

    def post(self, request):
        return redirect('view_inventory')

    def get(self, request):
        # print()
        return HttpResponseRedirect(f'/view_inventory{request.get_full_path()[1:]}')


def store_inventory(request):

    products = None
    categories = Category.get_all_categories()
    category_id = request.GET.get('category')
    print(f"You have selected {category_id} category")
    if category_id:
        products = Product.get_all_products_by_categoryid(category_id)
    else:
        products = Product.get_all_products()

    data = dict({})
    data['products'] = products
    data['categories'] = categories

    print('you are : ', request.session.get('email'))
    return render(request, 'view_inventory', data)