from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings
from .validators import validate_file_extension
# Create your models here.


class User(AbstractUser):
    profile_image = models.ImageField(upload_to='images/', default='images/image.jpg')


class SiteConfiguration(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    site_name = models.CharField(max_length=50,default="")
    site_email = models.EmailField(max_length=50,default="")
    site_favicon = models.ImageField(upload_to='images/',validators=[validate_file_extension],default="")
    site_logo = models.ImageField(upload_to='images/',validators=[validate_file_extension],default="")
    site_address = models.CharField(max_length=200,default="")
    copy_right = models.CharField(max_length=50,default="")
   
    def __str__(self):
        return self.site_name

class SmtpConfiguration(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    smtp_email = models.EmailField(max_length=50,default="")
    smtp_password = models.CharField(max_length=50,default="")

    def __str__(self):
        return self.smtp_email
