import glob

from django.shortcuts import render, redirect, HttpResponseRedirect, get_object_or_404
from store.models.products import Product
from store.models.category import Category
from django.views import View
from store.forms import SingleInventoryForm #BulkInventoryForm
import shutil
import os
from PIL import Image
# Create your views here.

def manageinv_index(request):
    return render(request,'manage_inventory.html')

def handle_uploaded_xls(f):
    with open("static/new_inventory.xls", "wb+") as destination:
        for chunk in f.chunks():
            destination.write(chunk)


def save_images(file, category):
    print(file)
    print(f" The category after data store: {category}")
    temp_dir = f'media/temp/'
    if not os.path.isdir(f'media/products/{category}/'):
        os.mkdir(f'media/products/{category}/')
    dest_dir = f'media/products/{category}/'
    for jpgfile in glob.iglob(os.path.join(temp_dir, "*.jpeg")):
        if not os.path.exists(os.path.join(dest_dir, jpgfile, "*.jpeg")):
            shutil.copy2(jpgfile, dest_dir)


    #shutil.copy2(f'{file}', img_directory)
    shutil.rmtree('media/temp/')

def add_inventory(request):
    context = {}
    single_inv_form = SingleInventoryForm()
    #bulk_inv_form = BulkInventoryForm()
    if request.method == 'POST':
        #if 'single_inv' in request.POST:
        form = SingleInventoryForm(request.POST, request.FILES)
        if form.is_valid():
            product_name = form.cleaned_data['name']
            product_category = form.cleaned_data['category']
            price = form.cleaned_data['price']
            quantity_purchased = form.cleaned_data['qty_purchased']
            quantity_sold = form.cleaned_data['qty_sold']
            quantity_available = form.cleaned_data['qty_available']
            image = request.FILES['image']
            category_id = get_object_or_404(Category, name=product_category)
            category = Category(category_id.pk)
            product_data = Product(name=product_name, category=category, price=price,
                                   qty_purchased=quantity_purchased,
                                   qty_sold=quantity_sold,
                                   qty_available=quantity_available, image=image)
            product_data.save()
            save_images(image, product_category)

        # if 'bulk_inv' in request.POST:
        #     form = BulkInventoryForm(request.POST)
        #     if form.is_valid():
        #         form.save()


    context = {
        'single_inv_form': single_inv_form,
        #'bulk_inv_form': bulk_inv_form
    }

    return render(request, "add_inventory.html", context)


