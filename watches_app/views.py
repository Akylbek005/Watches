from django.shortcuts import render, get_object_or_404
from django.core.mail import send_mail
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .forms import ContactForm
from watches.settings import EMAIL_HOST_USER

from .models import Category, Colors, Sizes, Product


def brands(request):
    return render(request, 'watches/brands.html')


def index(request):
    return render(request, 'watches/index.html')


def checkout(request):
    return render(request, 'watches/checkout.html')


def login(request):
    return render(request, 'watches/login.html')


def product_detail(request, slug, category):
    product = get_object_or_404(Product, slug=slug)
    recommendation_products = Product.objects.filter(category__slug=category)

    return render(request, 'watches/product_detail.html', {'product': product,
                                                           'recommendation_products': recommendation_products})


def product_list(request):
    categories = Category.objects.all()
    colors = Colors.objects.all()
    sizes = Sizes.objects.all()
    products = Product.objects.all()[::-1]

    if request.GET.get('category'):
        category = request.GET.get('category')
        products = Product.objects.filter(category__slug=category)

    elif request.GET.get('color'):
        color = request.GET.get('color')
        products = Product.objects.filter(color__slug=color)

    elif request.GET.get('size'):
        size = request.GET.get('size')
        products = Product.objects.filter(size__slug=size)

    return render(request, 'watches/product_list.html', {'categories': categories,
                                                         'colors': colors,
                                                         'sizes': sizes,
                                                         'products': products})


def register(request):
    return render(request, 'watches/register.html')


def news(request):
    return render(request, 'watches/news.html')


def contact(request):
    if request.method == 'POST':
        contact = ContactForm(request.POST)
        if contact.is_valid():
            subject = contact.cleaned_data.get('subject')
            email = contact.cleaned_data.get('email')
            message = contact.cleaned_data.get('message')
            name = contact.cleaned_data.get('name')
            send_mail(f'Отзыв от {name}.Тема отзыва: {subject}',
                      f'{message}\n'
                      f'Email пользователя - {email}',
                      EMAIL_HOST_USER,
                      [EMAIL_HOST_USER, ])
        return render(request, 'watches/contact.html', {'form': 'Отзыв успешно отправлен'})
    else:
        return render(request, 'watches/contact.html')
