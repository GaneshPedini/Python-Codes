from django.shortcuts import render, redirect, HttpResponseRedirect
from store.models.garcy_store import Garcy_Store



# Create your viewa
def home(request):
    data = {}
    stores = Garcy_Store.get_all_stores()
    data['stores'] = stores
    print(data)
    return render(request,'home.html', data)
# <a href="{% url 'store' store.id %}"
def store(request, id):
    data = dict({})
    data['store'] = Garcy_Store.get_store_by_id(id)
    print(id)
    return render(request, 'store.html', data)




