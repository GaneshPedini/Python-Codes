# Generated by Django 5.0.1 on 2024-02-26 22:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0021_alter_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, upload_to='products/'),
        ),
    ]
