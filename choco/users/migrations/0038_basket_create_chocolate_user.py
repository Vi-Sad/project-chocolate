# Generated by Django 4.2.1 on 2024-07-30 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0037_orders'),
    ]

    operations = [
        migrations.AddField(
            model_name='basket',
            name='create_chocolate_user',
            field=models.BooleanField(default=False),
        ),
    ]
