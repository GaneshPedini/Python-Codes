from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)

    @staticmethod
    def get_categories_by_id(ids):
        return Category.objects.filter(id=ids)
    @staticmethod
    def get_all_categories():
        return Category.objects.all()

    @staticmethod
    def get_id_by_name(name):
        single_obj = Category.get_object_or_404(name=name)
        return single_obj.pk

    def __str__(self):
        return self.name