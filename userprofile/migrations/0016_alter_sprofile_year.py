# Generated by Django 4.1 on 2022-11-19 13:26

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0015_alter_sprofile_branch'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sprofile',
            name='year',
            field=models.PositiveIntegerField(default=1, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(4)]),
        ),
    ]
