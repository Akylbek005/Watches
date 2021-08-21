from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),

    path('brands/', views.brands, name='brands'),
    path('contact/', views.contact, name='contact'),
    path('checkout/', views.checkout, name='checkout'),
    path('news/', views.news, name='news'),

    path('all/', views.product_list, name='product_list'),
    path('<str:category>/<str:slug>/', views.product_detail, name='product_detail'),

    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
]
