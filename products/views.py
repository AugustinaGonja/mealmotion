from django.shortcuts import render
from .models import Product,Category

# Create your views here.

def product_list(request):
    """ View to display list of products."""
    products = Product.objects.all()
    total_products = products.count()

    context = {
        'products': products,
        'total_products': total_products,
    }
    return render(request, 'products/products.html', context)


def product_details(request, product_id):
    """ View to display a specific product's details."""
    product = Product.objects.get(id=product_id)
    context = {
        'product': product,
    }
    return render(request, 'products/product_details.html', context)
