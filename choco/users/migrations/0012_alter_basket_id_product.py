# Generated by Django 4.2.1 on 2024-05-05 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0011_basket_id_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basket',
            name='id_product',
            field=models.IntegerField(default=0, unique=True),
        ),
    ]
