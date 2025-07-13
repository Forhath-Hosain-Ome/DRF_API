from django.db import models
from models import BaseModel, GenderChoice, CourseModel

class StudentModel(BaseModel):
    name = models.CharField(max_length=20)
    age = models.IntegerField(max_length=2, blank=True, null=True)
    phone_number = models.IntegerField(max_length=20, unique=True, blank=True, null=True)
    email = models.EmailField(unique=True, blank=True, null=True)
    address = models.TextField(max_length=30, null=True)
    gender = models.CharField(choices=GenderChoice.choices, default='', null=True)
    course = models.ForeignKey(CourseModel, on_delete=models.CASCADE)
    profile_image = models.ImageField(upload_to='/resourses/{self.title}')
    fathers_name = models.CharField(max_length=20, null=True)
    mothers_name = models.CharField(max_length=20, null=True)