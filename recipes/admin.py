from django.contrib import admin
from .models import Recipe, Category

# Register your models here.

class RecipeAdmin(admin.ModelAdmin):
    list_display = ('name', 'get_categories', 'rating')
    search_fields = ('name', 'ingredients', 'instructions')
    list_filter = ('categories',)
    ordering=('name',)

    # Shows all categories assigned to a recipe 
    
    def get_categories(self, obj):
        return ", ".join([c.name for c in obj.categories.all()])
    get_categories.short_description = 'Categories'

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'friendly_name')
    search_fields = ('name',)

admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Category, CategoryAdmin)
