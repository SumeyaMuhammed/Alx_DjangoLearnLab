from django.db import models
from django.conf import settings
from django.utils import timezone

User = settings.AUTH_USER_MODEL
class Post(models.Model):
  author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
  title = models.CharField(max_length=200)
  content = models.TextField()
  created_at = models.DateTimeField(default=timezone.now)
  updated_at = models.DateTimeField(auto_now=True)

  class Meta:
    ordering = ['-created_at']

  def __str__(self):
    return f"{self.title} (by {self.author})"

class Comment(models.Model):
  Post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
  User = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
  content = models.TextField()
  created_at = models.DateTimeField(default=timezone.now)
  updated_at = models.DateTimeField(auto_now=True)

  class Meta:
    ordering = ['created_at']

  def __str__(self):
    return f"Comment by {self.author} on {self.post}"

class Like(models.Model):
  post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='like')
  author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='like')
  created_at = models.DateTimeField(auto_now_add=True)

  class Meta:
        unique_together = ('post', 'author')  # prevents multiple likes