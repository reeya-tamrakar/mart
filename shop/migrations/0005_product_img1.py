# Generated by Django 3.1.3 on 2020-12-28 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_product_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='img1',
            field=models.ImageField(default=1, upload_to='shop/products'),
            preserve_default=False,
        ),
    ]
