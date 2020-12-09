from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="ShopHomePage"),
    path('index', views.index, name="ShopHomePage"),
    path('cart', views.cart, name="Cart"),
    path('blog-single-sidebar', views.blog, name="Blog"),
    path('checkout', views.checkout, name="Blog"),
    path('contact', views.contact, name="Contact"),
    path('shop-grid', views.shopgrid, name="ShopGrid"),
]
