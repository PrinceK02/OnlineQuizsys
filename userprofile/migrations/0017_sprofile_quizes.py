# Generated by Django 4.1 on 2022-11-20 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0002_quizze_time'),
        ('userprofile', '0016_alter_sprofile_year'),
    ]

    operations = [
        migrations.AddField(
            model_name='sprofile',
            name='quizes',
            field=models.ManyToManyField(to='quiz.quizze'),
        ),
    ]
