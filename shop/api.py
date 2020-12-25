from django.http import JsonResponse
from django.core import serializers
from .models import Product

def fetch_products(request):
    products = Product.objects.all()
    products_json = serializers.serialize('json', products)
    return JsonResponse(products_json, safe=False)
