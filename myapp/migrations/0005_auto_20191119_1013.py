# Generated by Django 2.2.6 on 2019-11-19 10:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_auto_20191119_1003'),
    ]

    operations = [
        migrations.RenameField(
            model_name='siteconfiguration',
            old_name='site_user',
            new_name='user',
        ),
        migrations.RenameField(
            model_name='smtpconfiguration',
            old_name='smtp_user',
            new_name='user',
        ),
    ]
