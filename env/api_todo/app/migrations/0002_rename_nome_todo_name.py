# Generated by Django 5.1.3 on 2024-11-07 18:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='todo',
            old_name='nome',
            new_name='name',
        ),
    ]
