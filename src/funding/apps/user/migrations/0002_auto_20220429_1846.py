# Generated by Django 2.1.7 on 2022-04-29 09:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pocket',
            old_name='is_activate',
            new_name='is_active',
        ),
    ]
