# Generated by Django 5.0.1 on 2024-01-14 19:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_product_qty_available_product_qty_purchased_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='qty_sold',
        ),
    ]
