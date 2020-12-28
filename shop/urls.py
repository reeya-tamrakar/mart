from django.urls import path
from django.conf.urls.static import static
from . import views
from .api import fetch_products
from mart import settings

urlpatterns = [
    path('', views.index, name="ShopHomePage"),
    path('index', views.index, name="ShopHomePage"),
    path('cart', views.cart, name="Cart"),
    path('blog-single-sidebar', views.blog, name="Blog"),
    path('checkout', views.checkout, name="Blog"),
    path('contact', views.contact, name="Contact"),

    path('shop-grid', views.shopgrid, name="ShopGrid"),
    path('api/fetch-products', fetch_products, name="fetchProduct"),

    path('products', views.products, name="ProductsPage"),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
