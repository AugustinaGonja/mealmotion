from django.shortcuts import render
from .models import Recipe

# Create your views here.
def recipe_list(request):
    """ View to display list of recipes , enabling both search and filter functionality."""
    recipes = Recipe.objects.all()
    
    context = {
        'recipes' : recipes
    }

    return render(request, 'recipes/recipes.html', context)
