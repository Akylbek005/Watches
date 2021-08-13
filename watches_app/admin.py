from django.contrib import admin
from .models import Product, Category, Colors, Sizes


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', )


@admin.register(Category)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')


@admin.register(Colors)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('color', )


@admin.register(Sizes)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('size', )
