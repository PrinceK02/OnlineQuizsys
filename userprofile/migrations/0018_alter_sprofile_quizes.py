# Generated by Django 4.1 on 2022-11-20 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0002_quizze_time'),
        ('userprofile', '0017_sprofile_quizes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sprofile',
            name='quizes',
            field=models.ManyToManyField(blank=True, to='quiz.quizze'),
        ),
    ]
