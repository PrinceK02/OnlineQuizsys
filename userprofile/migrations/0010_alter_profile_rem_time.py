# Generated by Django 4.1 on 2022-09-30 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0009_profile_contact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='rem_time',
            field=models.IntegerField(default=3600),
        ),
    ]
