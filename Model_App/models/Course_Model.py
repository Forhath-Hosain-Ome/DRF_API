from django.db import models
from Model_App.models import BaseModel
from core.utilities import UploadPath

class CourseModel(BaseModel):
    title = models.CharField(max_length=25, unique=True)
    description = models.TextField(max_length=80)
    profile_image = models.ImageField(upload_to=UploadPath)
    cover_image = models.ImageField(upload_to=UploadPath)
    instructors = models.ForeignKey('Model_App.AccountModel', on_delete=models.CASCADE, limit_choices_to = { 'is_instructors' : True }, related_name='Course_Teacher')
    Coordinator = models.OneToOneField('Model_App.AccountModel', on_delete=models.CASCADE, limit_choices_to = { 'is_Coordinator' : True }, related_name='Course_Coordinator')
    assistant = models.ForeignKey('Model_App.AccountModel', on_delete=models.CASCADE, limit_choices_to = { 'is_assistant' : True }, related_name='Course_Assistant')
    available_sit = models.PositiveIntegerField()

    class Meta:
        db_table = 'CourseModel'
        verbose_name = 'CourseModel'
        verbose_name_plural = 'CourseModels'
        ordering = ['title', 'Course_Teacher', 'Course_Coordinator', 'Course_Assistant', 'available_sit']