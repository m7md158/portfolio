# Generated by Django 5.1.1 on 2024-09-08 11:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0003_profile_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='middle_name',
            new_name='nickname',
        ),
    ]
