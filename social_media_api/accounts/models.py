from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
  bio = models.TextField(max_length=400)
  profile_picture = models.ImageField()
  followers = models.ManyToManyField('self', symmetrical=False, related_name='following_users')
  following = models.ManyToManyField('self', symmetrical=False, related_name='follower_users')


