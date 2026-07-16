from django.shortcuts import render

# Create your views here.

def shop_details(request):

    return render(request,"shop/shop_details.html")