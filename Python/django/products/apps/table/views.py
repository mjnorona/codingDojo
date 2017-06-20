from django.shortcuts import render
from .models import Product
# Create your views here.
def index(request):
    Product.objects.create(name = "tv", description = "Cool LCD display", weight = "50", price = "70.99", cost = "30.99", category = "technology")
    Product.objects.create(name="guitar", description="B.C. Rich Bich", weight="10", price="99.99", cost="50.99",
                           category="music")
    Product.objects.create(name="shirt", description="Bright blue top", weight="1", price="20.99", cost="2.99",
                           category="clothing")
    products = Product.objects.all()
    for product in products:
        print product.name, product.description
    return render(request, 'table/index.html')