# Generated by Django 4.2.1 on 2024-04-29 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_alter_user_email_alter_user_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='basket',
            name='favourites',
            field=models.BooleanField(default=False),
        ),
    ]
