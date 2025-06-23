from django.db import models

# Create your models here.
class note(models.Model):
    title = models.CharField(max_length=20, unique=True)
    content = models.TextField(max_length=99)
    created_at = models.DateTimeField(auto_now=True)