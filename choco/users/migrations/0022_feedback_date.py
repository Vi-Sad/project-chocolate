# Generated by Django 4.2.1 on 2024-05-09 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0021_feedback_anonim'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedback',
            name='date',
            field=models.DateField(default=None),
        ),
    ]
