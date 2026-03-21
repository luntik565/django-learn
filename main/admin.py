from django.contrib import admin
from .models import Category, Product

@admin.register(Category)
class CatAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Product)
class ProdAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'price', 'avaliable', 'create', 'update']
    list_filter = ['category', 'avaliable', 'create', 'update']
    list_editable = ['price', 'avaliable']
    prepopulated_fields = {'slug': ('name', )}
    