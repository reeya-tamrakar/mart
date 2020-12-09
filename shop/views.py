from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'shop/index.html')

def cart(request):
    return render(request, 'shop/cart.html')

def blog(request):
    return render(request, 'shop/blog-single-sidebar.html')

def checkout(request):
    return render(request, 'shop/checkout.html')

def contact(request):
    return render(request, 'shop/contact.html')

def shopgrid(request):
    return render(request, 'shop/shop-grid.html')
