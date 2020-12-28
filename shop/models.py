from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=1000)
    price = models.FloatField()
    # img1 = models.ImageField(upload_to="shop/products")
    in_stock = models.BooleanField(default=True)

    def __str__(self):
        return self.name
