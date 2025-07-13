from django.db import models

class BaseModel(models.Model):
    is_student = models.BooleanField(default=True)
    is_Coordinator = models.BooleanField(default=True)
    is_assistant = models.BooleanField(default=False)
    is_instructors = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True