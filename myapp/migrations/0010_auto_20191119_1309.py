# Generated by Django 2.2.6 on 2019-11-19 13:09

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0009_auto_20191119_1226'),
    ]

    operations = [
        migrations.AlterField(
            model_name='site',
            name='user',
            field=models.ForeignKey(null=True, on_delete=True, related_name='site_user', to=settings.AUTH_USER_MODEL),
        ),
    ]
