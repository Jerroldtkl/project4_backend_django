# Generated by Django 3.2.8 on 2021-10-14 07:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_information', '0004_auto_20211014_1538'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='email',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='password',
        ),
    ]
