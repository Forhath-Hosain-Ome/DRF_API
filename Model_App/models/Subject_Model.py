from django.db import models
from Model_App.models import TimeStamp

class SubjectModel(TimeStamp):
    title = models.CharField(max_length=30, unique=True)
    subject_code = models.CharField(max_length=12, unique=True)
    depertment = models.ManyToManyField('Model_App.CourseModel', related_name='Course_Subject')

    class Meta:
        db_table = 'SubjectModel'
        verbose_name = 'SubjectModel'
        verbose_name_plural = 'SubjectModels'
        ordering = ['title', 'subject_code']

    def __str__(self):
        return f'{self.title} Depertment Is {self.depertment}'