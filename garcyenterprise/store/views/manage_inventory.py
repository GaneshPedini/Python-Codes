from django.shortcuts import render, redirect, HttpResponseRedirect
from store.models.products import Product
from store.models.category import Category
from django.views import View
from store.forms import InventoryForm

# Create your views here.

def manageinv_index(request):
    return render(request,'manage_inventory.html')

def add_single_product(request):
    context = {}
    if request.method == 'POST':
        form = InventoryForm(request.POST)
        if form.is_valid():
            product_name = form.cleaned_data['product_name']
            product_category = form.cleaned_data['product_category']
            price = form.cleaned_data['price']
            quantity_purchased = form.cleaned_data['quantity_purchased']
            quantity_sold = form.cleaned_data['quantity_sold']
            quantity_available = form.cleaned_data['quantity_available']
            category = Category(product_category)
            product_data = Product(name=product_name, category=category, price=price,
                                   qty_purchased=quantity_purchased,
                                   qty_sold=quantity_sold,
                                   qty_available=quantity_available)
            product_data.save()

    else:

        context['form'] = InventoryForm()

    return render(request, "add_single_product.html", context)
