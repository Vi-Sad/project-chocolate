# Generated by Django 4.2.1 on 2024-05-05 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_alter_product_product_name'),
        ('users', '0013_remove_basket_name_basket_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='basket',
            name='id_product',
        ),
        migrations.AddField(
            model_name='basket',
            name='id_product',
            field=models.ManyToManyField(to='main.product'),
        ),
    ]
