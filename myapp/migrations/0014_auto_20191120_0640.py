# Generated by Django 2.2.6 on 2019-11-20 06:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import myapp.validators


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0013_auto_20191120_0615'),
    ]

    operations = [
        migrations.AlterField(
            model_name='siteconfiguration',
            name='copy_right',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='siteconfiguration',
            name='site_address',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='siteconfiguration',
            name='site_email',
            field=models.EmailField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='siteconfiguration',
            name='site_favicon',
            field=models.ImageField(default='', upload_to='images/', validators=[myapp.validators.validate_file_extension]),
        ),
        migrations.AlterField(
            model_name='siteconfiguration',
            name='site_logo',
            field=models.ImageField(default='', upload_to='images/', validators=[myapp.validators.validate_file_extension]),
        ),
        migrations.AlterField(
            model_name='siteconfiguration',
            name='site_name',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='siteconfiguration',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='smtpconfiguration',
            name='smtp_email',
            field=models.EmailField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='smtpconfiguration',
            name='smtp_password',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='smtpconfiguration',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]