# Generated by Django 3.2.8 on 2021-11-09 22:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import ecommerce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=100)),
                ('category_slug', models.SlugField()),
                ('category_image', models.ImageField(default=None, upload_to=ecommerce.models.category_image_path)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=100)),
                ('product_brand', models.CharField(max_length=100)),
                ('product_description', models.TextField(max_length=500)),
                ('product_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('product_image_1', models.ImageField(default=None, upload_to=ecommerce.models.product_image_path1)),
                ('product_image_2', models.ImageField(default=None, upload_to=ecommerce.models.product_image_path2)),
                ('product_category', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='ecommerce.category')),
                ('product_seller', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_time', models.DateTimeField()),
                ('payment_product', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='ecommerce.product')),
                ('payment_user', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
