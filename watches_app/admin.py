from django.contrib import admin
from .models import *


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


@admin.register(EmailNewsLetter)
class EmailNewsLetterAdmin(admin.ModelAdmin):
    list_display = ('email', )
