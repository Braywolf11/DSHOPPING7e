# Generated by Django 2.2.5 on 2019-10-19 01:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administration', '0002_shopping'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shopping',
            name='shopping_date',
            field=models.DateField(auto_now=True, verbose_name='Shopping_date'),
        ),
    ]
