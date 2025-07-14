from django.db import models
from Model_App.models import TimeStamp



class DepertmentModel(TimeStamp):
    name = models.CharField(max_length=20, unique=True)
    description = models.TextField(max_length=30)
    coordinator = models.ForeignKey('Model_App.AccountModel', limit_choices_to = { 'role' : 'coordinator' }, on_delete=models.CASCADE, related_name='Depertment_Head')
    instructors = models.ManyToManyField('Model_App.AccountModel', limit_choices_to = { 'role' : 'instructor' }, related_name='Depertment_Teacher')
    assistant = models.ManyToManyField('Model_App.AccountModel', limit_choices_to = { 'role' : 'assistant' }, related_name='Depertment_Assistant')

    class Meta:
        db_table = 'DepertmentModel'
        verbose_name = 'DepertmentModel'
        verbose_name_plural = 'DepertmentModels'
        ordering = ['name']

    def __str__(self):
        return f'{self.name} Coordinator Is {self.coordinator}'