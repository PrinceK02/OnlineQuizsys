# Generated by Django 4.1 on 2022-11-21 10:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('leaderboard', '0004_remove_leaderboard_quiz'),
        ('quiz', '0002_quizze_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='quizze',
            name='lb',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='leaderboard.leaderboard'),
        ),
    ]
