from django.db import models

class StatusModel(models.Model):
    is_active = models.BooleanField(default=False)
    is_pending = models.BooleanField(default=False)
    is_completed = models.BooleanField(default=False)

    class Meta:
        abstract = True