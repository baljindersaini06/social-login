from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings
from .validators import validate_file_extension

# Create your models here.


class User(AbstractUser):
    profile_image = models.ImageField(upload_to='images/')


class SiteConfiguration(models.Model):
    site_name = models.CharField(max_length=50)
    site_email = models.EmailField(max_length=50)
    site_favicon = models.ImageField(upload_to='images/',validators=[validate_file_extension])
    site_logo = models.ImageField(upload_to='images/',validators=[validate_file_extension])
    site_address = models.CharField(max_length=200)
    copy_right = models.CharField(max_length=50)
   
    def __str__(self):
        return self.site_name

class SmtpConfiguration(models.Model):
    smtp_email = models.EmailField(max_length=50)
    smtp_password = models.CharField(max_length=50)

    def __str__(self):
        return self.smtp_email