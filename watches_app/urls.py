from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('brands/', brands, name='brands'),
    path('contact/', contact, name='contact'),
    path('checkout/', checkout, name='checkout'),
    path('login/', login, name='login'),
    path('single/', single, name='single'),
    path('men/', men, name='men'),
    path('register/', register, name='register')
]
