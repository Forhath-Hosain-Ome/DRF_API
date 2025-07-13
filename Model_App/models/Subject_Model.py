from django.db import models
from models import BaseModel, DepertmentModel

class SubjectModel(BaseModel):
    title = models.CharField(max_length=30, unique=True)
    subject_code = models.CharField(max_length=12, unique=True)
    depertment = models.ForeignKey(DepertmentModel, on_delete=models.CASCADE)