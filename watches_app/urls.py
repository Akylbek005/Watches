from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),

    path('brands/', brands, name='brands'),
    path('contact/', contact, name='contact'),
    path('checkout/', checkout, name='checkout'),
    path('news/', news, name='news'),

    path('all/', product_list, name='product_list'),
    path('<str:category>/<str:slug>/', product_detail, name='product_detail'),

    path('login/', login, name='login'),
    path('register/', register, name='register'),
]
