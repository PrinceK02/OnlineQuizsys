# Generated by Django 2.1.2 on 2018-11-17 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theory', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='choice',
            name='question',
        ),
        migrations.RemoveField(
            model_name='answer',
            name='choice',
        ),
        migrations.AddField(
            model_name='answer',
            name='desc',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.DeleteModel(
            name='Choice',
        ),
    ]