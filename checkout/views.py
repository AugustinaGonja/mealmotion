from django.shortcuts import render,redirect,reverse
from django.contrib import messages
from .forms import OrderForm

# Create your views here.

def checkout(request):
    bag= request.session.get('bag', {})
    if not bag :
        messages.error (request , "There are currently no items in you bag")
        return redirect(reverse('products'))
    
    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form' : order_form,
        'stripe_public_key':'pk_test_51SMD593tTpk7jS1c1xAJiLXY02RppwLP2DlYOxiKPJUjsqEnBBymkOL8hvEfwq89PKuwSs68l1g8mTvNp2DOogJ300cfo2JfG6',
        'client_secret':'test_client_secret',
    }

    return render(request, template, context)