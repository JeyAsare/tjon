# Generated by Django 3.2.25 on 2024-06-24 06:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_product_has_sizes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='has_sizes',
        ),
    ]
