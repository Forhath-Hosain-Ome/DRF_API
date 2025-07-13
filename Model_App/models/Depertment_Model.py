from django.db import models
from models import BaseModel, TeacherModel


class DepertmentModel(BaseModel):
    name = models.CharField(max_length=20, unique=True)
    description = models.TextField(max_length=30)
    depertmentHead = models.ForeignKey(TeacherModel, on_delete=models.CASCADE)
    instructors = models.ManyToManyField(TeacherModel)