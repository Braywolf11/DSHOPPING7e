# Generated by Django 2.2.5 on 2019-10-19 01:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administration', '0004_auto_20191019_0112'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shopping',
            name='shopping_date',
            field=models.DateField(auto_now=True, verbose_name='Shopping_date'),
        ),
    ]
