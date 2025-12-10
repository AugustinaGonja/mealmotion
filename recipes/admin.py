from django.contrib import admin
from .models import Recipe, Category

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'categories', 'rating')
    search_fields = ('name', 'ingredients', 'instructions')
    list_filter = ('categories',)
    ordering=('name',)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'friendly_name')
    search_fields = ('name',)

admin.site.register(Recipe)
admin.site.register(Category)
