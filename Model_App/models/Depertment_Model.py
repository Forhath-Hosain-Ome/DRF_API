from django.db import models
from Model_App.models import BaseModel



class DepertmentModel(BaseModel):
    name = models.CharField(max_length=20, unique=True)
    description = models.TextField(max_length=30)
    depertmentHead = models.ForeignKey('Model_App.AccountModel', limit_choices_to = { 'is_Coordinator' : True }, on_delete=models.CASCADE, related_name='Depertment_Head')
    instructors = models.ManyToManyField('Model_App.AccountModel', limit_choices_to = { 'is_instructor' : True }, related_name='Depertment_Teacher')
    assistant = models.ManyToManyField('Model_App.AccountModel', limit_choices_to = { 'is_assistant' : True }, related_name='Depertment_Assistant')

    class Meta:
        db_table = 'DepertmentModel'
        verbose_name = 'DepertmentModel'
        verbose_name_plural = 'DepertmentModels'
        ordering = ['name']