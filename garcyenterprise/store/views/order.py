from django.shortcuts import render, redirect, HttpResponseRedirect
from store.models.products import Product
from store.models.category import Category
from django.views import View
from store.forms import SingleInventoryForm, BulkInventoryForm

# Create your views here.

def order_index(request):
    return render(request,'order.html')