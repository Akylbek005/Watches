# Generated by Django 3.2.5 on 2021-08-17 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('watches_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='gender',
            field=models.CharField(choices=[('man', 'Мужской'), ('woman', 'Женский')], default='man', max_length=16),
        ),
        migrations.AddField(
            model_name='product',
            name='slug',
            field=models.SlugField(default='ok', max_length=32),
            preserve_default=False,
        ),
    ]