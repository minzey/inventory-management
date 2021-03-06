# Generated by Django 4.0.1 on 2022-01-19 01:44

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='active',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='item',
            name='count',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)]),
        ),
    ]
