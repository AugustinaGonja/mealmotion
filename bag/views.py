from django.shortcuts import render

# Create your views here.

def shopping_bag(request):
    """ View rendering shopping bag page """

    return render(request, 'bag/shopping_bag.html')