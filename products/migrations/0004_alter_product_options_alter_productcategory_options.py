# Generated by Django 4.1.7 on 2023-05-06 17:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_basket'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name': 'Продукт', 'verbose_name_plural': 'Продукты'},
        ),
        migrations.AlterModelOptions(
            name='productcategory',
            options={'verbose_name': 'категория', 'verbose_name_plural': 'категории'},
        ),
    ]
