# Generated by Django 4.1.2 on 2022-10-11 10:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profiles',
            name='unique_id',
        ),
        migrations.RemoveField(
            model_name='subscriptions',
            name='unique_id',
        ),
    ]
