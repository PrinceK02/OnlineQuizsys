# Generated by Django 4.1 on 2022-11-19 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0002_alter_tprofile_contact_alter_tprofile_year'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tprofile',
            name='status',
            field=models.CharField(choices=[('Student', 'Student'), ('Teacher', 'Teacher')], max_length=255),
        ),
    ]
