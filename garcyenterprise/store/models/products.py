from django.db import models
from .category import Category


class Product(models.Model):
    name = models.CharField(max_length=60)
    price = models.IntegerField(default=0)
    qty_purchased = models.IntegerField(default=0)
    qty_available = models.IntegerField(default=0)
    qty_sold = models.IntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    image = models.ImageField(upload_to='media/products/')
    #category = models.ForeignKey(Category, to_field="id", related_name="category", on_delete=models.CASCADE, default=1)
    #image = models.ImageField(upload_to='media/products/')


    @property
    def _qty_sold(self):
        qty_sold = self.qty_purchased - self.qty_available
        return qty_sold

    @staticmethod
    def get_products_by_id(ids):
        return Product.objects.filter(id__in=ids)

    @staticmethod
    def get_all_products():
        return Product.objects.all()

    @staticmethod
    def get_all_products_by_categoryid(category_id):
        if category_id:
            print(f"The category in model: {category_id}")
            data = Product.objects.filter(category=category_id)
            print(data)
            return Product.objects.filter(category=category_id)
        else:
            return Product.get_all_products()

    def save(self, *args, **kwargs):
        self.qty_sold= self._qty_sold
        super(Product, self).save(*args, **kwargs)

    # class Meta:
    #     ordering = ['name', 'firstname', 'middlename']