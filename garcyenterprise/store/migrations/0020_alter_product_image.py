# Generated by Django 5.0.1 on 2024-02-26 21:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0019_alter_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(upload_to='store/media/products/'),
        ),
    ]
