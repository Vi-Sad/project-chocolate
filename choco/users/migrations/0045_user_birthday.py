# Generated by Django 4.2.1 on 2024-08-05 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0044_feedbackimage_id_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='birthday',
            field=models.DateField(default=None, null=True),
        ),
    ]
