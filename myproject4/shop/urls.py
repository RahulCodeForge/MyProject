from django.urls import path
from . import views


urlpatterns = [
    
    path('',views.shop_details, name="shop_details"),
]
