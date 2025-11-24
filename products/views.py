from django.shortcuts import render, redirect,reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Product,Category

# Create your views here.

def product_list(request):
    """ View to display list of products , enabling both search and filter functionality."""
    
    products = Product.objects.all()
    total_products = products.count()
    query = None
    category_names = []
    category_objects = Category.objects.none()
    
    if 'category' in request.GET:
        category_names = request.GET['category'].split(',')
        products = products.filter(category__name__in=category_names)
        category_objects = Category.objects.filter(name__in=category_names)
        total_products = products.count()

    if 'q' in request.GET:
        query = request.GET.get('q')
        if not query:
            messages.error(request, "You didn't enter any search criteria!")
            return redirect(reverse('products'))

        queries = Q(name__icontains=query) | Q(description__icontains=query)
        products = products.filter(queries)
        total_products = products.count()

    context = {
        'products': products,
        'total_products': total_products,
        'search_term': query,
        'current_categories': category_names,
        'category_objects': category_objects,
    }
    return render(request, 'products/products.html', context)


def product_details(request, product_id):
    """ View to display a specific product's details."""
    product = Product.objects.get(id=product_id)
    context = {
        'product': product,
    }
    return render(request, 'products/product_details.html', context)