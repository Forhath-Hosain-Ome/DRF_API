from django.db import models

class TeacherModel(models.Model):
    name = models.CharField()
    teacher_id = models.IntegerField()
    depertment = models.CharField()

    def __str__(self):
        return self.name