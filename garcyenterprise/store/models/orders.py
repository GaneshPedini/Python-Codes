from django.db import models
from .products import Product
from .customers import Customer
from .garcy_store import Garcy_Store
from .category import Category
import datetime


class Order(models.Model):
    date = models.DateField(default=datetime.datetime.today)
    store = models.ForeignKey(Garcy_Store,
                                 on_delete=models.CASCADE)
    order_id = models.CharField(max_length=50) #concat(store_name, YYYYMMSSHHMM)
    category = models.ForeignKey(Category,
                                on_delete=models.CASCADE)
    product = models.ForeignKey(Product,
                                on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer,
                                 on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    price = models.IntegerField()
    address = models.CharField(max_length=50, default='', blank=True)
    phone = models.CharField(max_length=50, default='', blank=True)

    status = models.BooleanField(default=False)

    def placeOrder(self):
        self.save()

    @staticmethod
    def get_orders_by_customer(customer_id):
        return Order.objects.filter(customer=customer_id).order_by('-date')
