# Generated by Django 4.1.3 on 2022-11-17 02:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('the_game', '0002_alter_connect4game_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='connect4game',
            name='game_complete',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='connect4game',
            name='game_winner',
            field=models.CharField(blank=True, max_length=1, null=True),
        ),
    ]
