from django.db import models
from core.models import TimeStamp
from Model_App.models import CourseModel, SubjectModel, AccountModel

class StudentEnrollment(TimeStamp):
    Student = models.OneToOneField(AccountModel, on_delete=models.CASCADE)
    course = models.ForeignKey(CourseModel, on_delete=models.CASCADE)
    subjects = models.ForeignKey(SubjectModel, on_delete=models.CASCADE)

    class Meta:
        db_table = 'StudentEnrollment'
        verbose_name = 'StudentEnrollment'
        verbose_name_plural = 'StudentEnrollments'
        ordering = ['Student', 'course', 'subjects']

    def __str__(self):
        return f'{self.Student} Is {self.course}'
