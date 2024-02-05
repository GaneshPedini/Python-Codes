from django.db import models

class Garcy_Store(models.Model):
    name = models.CharField(max_length=50)

    @staticmethod
    def get_all_stores():
        return Garcy_Store.objects.all()

    def get_store_by_id(id):
        return Garcy_Store.objects.get(id=id)

    def __str__(self):
        return self.name