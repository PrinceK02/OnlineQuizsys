# Generated by Django 4.1 on 2022-11-21 10:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0002_quizze_time'),
        ('leaderboard', '0002_auto_20180903_1325'),
    ]

    operations = [
        migrations.AddField(
            model_name='leaderboard',
            name='quiz',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='quiz.quizze'),
        ),
    ]