from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User, AbstractUser, BaseUserManager
from django.dispatch import receiver


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_year = models.IntegerField()

    def __str__(self):
        return self.title
    
class CustomUserManager(BaseUserManager):
  def create_user(self, email, date_of_birth, profile_photo, password, **Other_fields):
    if not email:
      raise ValueError("Users must have an email address")
    user = self.model(email=self.normalize_email(email), date_of_birth=date_of_birth, profile_photo=profile_photo,  **Other_fields )
    user.set_password(password)
    user.save(using=self._db)
    return user

  def create_superuser(self, email, date_of_birth, profile_photo, password=None, **other_fields):
    user = self.create_user(
            email, profile_photo=profile_photo, date_of_birth=date_of_birth,
            password=password,
        )
    user.is_admin = True
    user.is_staff=True
    user.is_superuser=True
    user.save(using=self._db)
    return user
  
class CustomUser(AbstractUser):
  date_of_birth = models.DateField()
  profile_photo = models.ImageField()
  objects = CustomUserManager()

class UserProfile(models.Model):
  user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='user')
  role = models.CharField(max_length=200, choices=[('Admin','Admin'), 
                                                   ('Librarian','Librarian'), 
                                                   ('Member','Member')])
  '''
  First item → stored in the database ('Admin')
  Second item → shown in forms and admin ('Admin')
  '''

@receiver(post_save, sender=CustomUser)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
