from django.db import models
from .garcy_store import Garcy_Store
from .orders import Order
import datetime


class Payment(models.Model):
    date = models.DateField(default=datetime.datetime.today)
    store = models.ForeignKey(Garcy_Store,
                                 on_delete=models.CASCADE)
    order_id = models.ForeignKey(Order,
                                 on_delete=models.CASCADE)
    cash = models.IntegerField(default=0)
    phonepay = models.IntegerField(default=0)
    credit = models.IntegerField(default=0)
