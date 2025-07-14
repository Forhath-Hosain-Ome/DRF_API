from django.db import models

class RoleModel(models.TextChoices):
    STUDENT = 'student', 'Student'
    COORDINATOR = 'coordinator', 'Coordinator'
    ASSISTANT = 'assistant', 'Assistant'
    INSTRUCTOR = 'instructor', 'Instructor'