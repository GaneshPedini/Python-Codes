from django.contrib import admin
from .models.garcy_store import Garcy_Store
from .models.category import Category
from .models.store_users import Store_User
from .models.products import Product
from .models.orders import Order
from .models.payment import Payment
from .models.customers import Customer
# Register your models here.
admin.site.register(Garcy_Store)
admin.site.register(Category)
admin.site.register(Store_User)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(Payment)
admin.site.register(Customer)

