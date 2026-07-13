from django.urls import path

from . import views


urlpatterns = [
    
    path('/',views.Home,name="shop_home"),
    path('product/', views.Product, name="product"),
]
