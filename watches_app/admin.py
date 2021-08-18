from django.contrib import admin
from .models import Product, Category, Colors, Sizes


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', )
    prepopulated_fields = {'slug': ('name', 'category', 'gender')}


@admin.register(Category)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Colors)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('color', )
    prepopulated_fields = {'slug': ('color',)}


@admin.register(Sizes)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('size', )
