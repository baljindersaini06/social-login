# Generated by Django 2.2.6 on 2019-11-19 07:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='profile_image',
            field=models.ImageField(default='images/image.jpg', upload_to='images/'),
        ),
    ]
