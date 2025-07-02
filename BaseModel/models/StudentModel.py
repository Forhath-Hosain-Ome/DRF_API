from django.db import models


class StudentModels(models.Model):
    name = models.CharField()
    student_id = models.IntegerField()
    depertment = models.CharField()

    def __str__(self):
        return self.name