from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
  bio = models.CharField(max_length=400)
  profile_picture = models.ImageField()
  followers = models.ManyToManyField('self', symmetrical=False, related_name='following')
