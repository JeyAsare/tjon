# Generated by Django 3.2.25 on 2024-06-24 06:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20240621_1152'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='has_sizes',
            field=models.BooleanField(default=False, null=True),
        ),
    ]
