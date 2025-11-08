from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver

class Author(models.Model):
  name = models.CharField(max_length=200)

  def __str__(self):
    return self.name

class Book(models.Model):
  title = models.CharField(max_length=200)
  author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="author")

  def __str__(self):
    return self.name

class Library(models.Model):
  name = models.CharField(max_length=200)
  books = models.ManyToManyField(Book, related_name="books")

  def __str__(self):
    return self.name

class Librarian(models.Model):
  name = models.CharField(max_length=200)
  library = models.OneToOneField(Library, on_delete=models.CASCADE, related_name="library")

  def __str__(self):
    return self.name
  
class UserProfile(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE, name='user')
  role = models.CharField(max_length=200, choices=[('Admin','Admin'), 
                                                   ('Librarian','Librarian'), 
                                                   ('Member','Member')])
  
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)