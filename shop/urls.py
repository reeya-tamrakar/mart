from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="ShopHomePage"),
    path('profile/', views.profile, name="ShopProfilePage")
]
