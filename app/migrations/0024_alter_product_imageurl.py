# Generated by Django 4.2.5 on 2023-10-18 01:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0023_product_imageurl'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='imageURL',
            field=models.URLField(blank=True, null=True),
        ),
    ]
