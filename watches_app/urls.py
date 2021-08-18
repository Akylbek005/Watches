from django.urls import path, include
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('brands/', brands, name='brands'),
    path('contact/', contact, name='contact'),
    path('checkout/', checkout, name='checkout'),
    path('login/', login, name='login'),
    path('men/', men, name='men'),
    path('<str:category>/<str:slug>/', single, name='product_detail'),
    path('register/', register, name='register'),
    path('news/', news, name='news'),
]
