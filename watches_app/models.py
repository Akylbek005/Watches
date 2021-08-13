from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=32)
    email = models.EmailField()
    subject = models.CharField(max_length=64)
    message = models.TextField()


class Category(models.Model):
    name = models.CharField(max_length=32)
    slug = models.SlugField(max_length=32)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Sizes(models.Model):
    size = models.CharField(max_length=4)
    slug = models.SlugField(max_length=4)

    def __str__(self):
        return self.size

    class Meta:
        verbose_name = 'Размер'
        verbose_name_plural = 'Размеры'


class Colors(models.Model):
    color = models.CharField(max_length=16)
    slug = models.SlugField(max_length=16)

    def __str__(self):
        return self.color

    class Meta:
        verbose_name = 'Цвет'
        verbose_name_plural = 'Цвета'


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='category')
    color = models.ManyToManyField(Colors,)
    size = models.ManyToManyField(Sizes)

    name = models.CharField(max_length=32)
    price = models.PositiveIntegerField()
    description = models.TextField()
    available = models.BooleanField(default=True)
    images_1 = models.ImageField(upload_to='product/')
    images_2 = models.ImageField(upload_to='product/')
    images_3 = models.ImageField(upload_to='product/')
    images_4 = models.ImageField(upload_to='product/')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

