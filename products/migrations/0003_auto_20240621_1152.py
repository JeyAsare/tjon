# Generated by Django 3.2.25 on 2024-06-21 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_remove_product_image_url'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Categories'},
        ),
        migrations.AddField(
            model_name='category',
            name='friendly_name',
            field=models.CharField(blank=True, max_length=254, null=True),
        ),
    ]
