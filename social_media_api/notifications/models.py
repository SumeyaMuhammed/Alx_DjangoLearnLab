from django.db import models
from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

User = settings.AUTH_USER_MODEL
class Notification(models.Model):
  recipient = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notifiactions')
  actor = models.ForeignKey(User, on_delete=models.CASCADE)
  target_content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, null=True, blank=True)
  target_object_id = models.PositiveIntegerField(null=True, blank=True)
  target = GenericForeignKey('target_content_type', 'target_object_id')
  read = models.BooleanField(default=False)
  timestamp = models.DateTimeField(auto_now_add=True)
