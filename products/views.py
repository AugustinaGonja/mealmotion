from django.shortcuts import render, redirect,reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Product,Category
from django.db.models.functions import Lower
from .forms import ProductForm

# Create your views here.

def product_list(request):
    """ View to display list of products , enabling both search and filter functionality."""

    products = Product.objects.all()
    total_products = products.count()
    query = None
    category_names = []
    category_objects = Category.objects.none()
    sort = None
    direction = None

    if 'sort' in request.GET:
        sortkey = request.GET['sort']
        sort = sortkey
        if sortkey == 'name':
            sortkey = 'lower_name'
            products = products.annotate(lower_name=Lower("name"))

        if 'direction' in request.GET:
            direction = request.GET['direction']
            if direction == 'desc':
                sortkey = f'-{sortkey}'
        products = products.order_by(sortkey)
    
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
    
    current_sorting = f'{sort}_{direction}' 

    context = {
        'products': products,
        'total_products': total_products,
        'search_term': query,
        'current_categories': category_names,
        'category_objects': category_objects,
        'current_sorting':sort,
    }
    return render(request, 'products/products.html', context)


def product_details(request, product_id):
    """ View to display a specific product's details."""
    product = Product.objects.get(id=product_id)
    context = {
        'product': product,
    }
    return render(request, 'products/product_details.html', context)

def add_product(request):
    form = ProductForm()
    template = 'products/add_product.html'
    context = {
        'form':form,
    }

    return render(request, template, context)