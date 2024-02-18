from django.shortcuts import render, redirect, HttpResponseRedirect
from store.models.products import Product
from store.models.category import Category
from django.views import View
from store.forms import SingleInventoryForm, BulkInventoryForm

# Create your views here.

def manageinv_index(request):
    return render(request,'manage_inventory.html')

def handle_uploaded_xls(f):
    with open("static/new_inventory.xls", "wb+") as destination:
        for chunk in f.chunks():
            destination.write(chunk)

def add_inventory(request):
    context = {}
    single_inv_form = SingleInventoryForm()
    bulk_inv_form = BulkInventoryForm()
    if request.method == 'POST':
        if 'single_inv' in request.POST:
            form = SingleInventoryForm(request.POST)
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

        if 'bulk_inv' in request.POST:
            pass

    else:
        context = {
            'single_inv_form': single_inv_form,
            'bulk_inv_form': bulk_inv_form
        }

    return render(request, "add_inventory.html", context)


