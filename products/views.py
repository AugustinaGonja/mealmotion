from django.shortcuts import render, redirect,reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
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

@login_required
def add_product(request):
    """Add product to the store """

    if not request.user.is_superuser:
        return redirect(reverse('home'))
    
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'Successfully added a product!')
            return redirect(reverse('product_details', args=[product.id]))
        else:
            messages.error(request, 'Product not addded.Please try again.')
    form = ProductForm()
    template = 'products/add_product.html'
    context = {
        'form':form,
    }

    return render(request, template, context)

@login_required
def edit_product(request, product_id):
    """Edit Product in store """

    if not request.user.is_superuser:
        return redirect(reverse('home'))
    
    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated')
            return redirect(reverse('product_details', args=[product.id]))
        else:
            messages.error(request, 'Failed to update product.Try again.')
    else:       
        form = ProductForm(instance=product)
        messages.info(request, f'You are editing {product.name}')

    template = 'products/edit_product.html'
    context = {
        'form':form,
        'product':product,
    }

    return render(request, template, context)

@login_required
def delete_product(request, product_id):
    """Delete Product in store """
    if not request.user.is_superuser:
        return redirect(reverse('home'))
    
    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, 'Product deleted')
    return redirect(reverse('products'))