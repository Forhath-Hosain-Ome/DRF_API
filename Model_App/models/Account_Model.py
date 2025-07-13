from django.db import models
from Model_App.models import BaseModel, GenderChoice
from core.utilities import UploadPath


class AccountModel(BaseModel):
    name = models.CharField(max_length=20)
    age = models.IntegerField(blank=True, null=True)
    phone_number = models.IntegerField(unique=True, blank=True, null=True)
    email = models.EmailField(unique=True, blank=True, null=True)
    address = models.TextField(max_length=30, null=True)
    gender = models.CharField(choices=GenderChoice.choices, default='', null=True)
    course = models.ForeignKey('Model_App.CourseModel', on_delete=models.CASCADE, related_name='Course_Student')
    profile_image = models.ImageField(upload_to=UploadPath)
    fathers_name = models.CharField(max_length=20, null=True)
    mothers_name = models.CharField(max_length=20, null=True)

    class Meta:
        db_table = 'AccountModel'
        verbose_name = 'AccountModel'
        verbose_name_plural = 'AccountModels'
        ordering = ['name', 'gender', 'email', 'phone_number', 'course', 'Course_Student']