# Generated by Django 4.2.1 on 2024-07-12 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0029_remove_basket_name_remove_feedback_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserChocolate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hard_id', models.CharField(default=None, max_length=50)),
                ('count', models.IntegerField(default=1)),
                ('price', models.IntegerField(default=0)),
            ],
        ),
    ]