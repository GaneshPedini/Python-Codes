from django.shortcuts import render , redirect , HttpResponseRedirect
from django.views import View
from store.models.garcy_store import Garcy_Store


# Create your views here.
class Home(View):

    def index(self):
        data = {}
        stores = Garcy_Store.get_all_stores()
        data['stores'] = stores
        return render('home', data)
