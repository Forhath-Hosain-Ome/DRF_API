from django.db import models
from .StudentModel import StudentModels as student


class Notes(models.Model):
    title = models.CharField(max_length=20, unique=True)
    content = models.TextField(max_length=99)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title