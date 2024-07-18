# Generated by Django 4.2.1 on 2024-07-12 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0030_userchocolate'),
    ]

    operations = [
        migrations.AddField(
            model_name='userchocolate',
            name='additives',
            field=models.CharField(default=None, max_length=50),
        ),
        migrations.AddField(
            model_name='userchocolate',
            name='basic',
            field=models.CharField(default=None, max_length=50),
        ),
        migrations.AddField(
            model_name='userchocolate',
            name='chocolate',
            field=models.CharField(default=None, max_length=50),
        ),
    ]