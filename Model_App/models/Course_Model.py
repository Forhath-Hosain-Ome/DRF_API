from django.db import models
from models import BaseModel, TeacherModel


class CourseModel(BaseModel):
    title = models.CharField(max_length=25, unique=True)
    description = models.TextField(max_length=80)
    profile_image = models.ImageField(upload_to='/resourses/{self.title}')
    cover_image = models.ImageField(upload_to='/resourses/{self.title}')
    instructors = models.ForeignKey(TeacherModel, on_delete=models.CASCADE, limit_choices_to = { 'is_instructors' : True })
    Coordinator = models.OneToOneField(TeacherModel, on_delete=models.CASCADE, limit_choices_to ={ 'is_Coordinator' : True })
    assistant = models.ForeignKey(TeacherModel, on_delete=models.CASCADE, limit_choices_to ={ 'is_assistant' : True })
    available_sit = models.PositiveIntegerField(max_length=2)