from django.contrib import admin
from Model_App.models import AccountModel, CourseModel, DepertmentModel, SubjectModel, StudentEnrollment

admin.site.register(AccountModel)
admin.site.register(CourseModel)
admin.site.register(DepertmentModel)
admin.site.register(SubjectModel)
admin.site.register(StudentEnrollment)