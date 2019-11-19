from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings

# Create your models here.


class User(AbstractUser):
    profile_image = models.ImageField(upload_to='images/', default='images/image.jpg')   