from django.shortcuts import render
from .models import Product

def ProductView(request):

    get_products = Product.objects.all()

    return render(request, 'product.html', {'products': get_products})