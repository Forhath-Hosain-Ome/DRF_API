from django.db import models
from Model_App.models import GenderChoice, TimeStamp, RoleModel
from core.utilities import UploadPath


class AccountModel(TimeStamp):
    name = models.CharField(max_length=20)
    age = models.IntegerField(blank=True, null=True)
    phone_number = models.IntegerField(unique=True, blank=True, null=True)
    email = models.EmailField(unique=True, blank=True, null=True)
    address = models.TextField(max_length=30, null=True)
    gender = models.CharField(choices=GenderChoice.choices, default='', null=True)
    profile_image = models.ImageField(upload_to=UploadPath, null=True, blank=True)
    fathers_name = models.CharField(max_length=20, null=True, blank=True)
    mothers_name = models.CharField(max_length=20, null=True, blank=True)
    role = models.CharField(choices=RoleModel.choices, default=RoleModel.STUDENT)

    class Meta:
        db_table = 'AccountModel'
        verbose_name = 'AccountModel'
        verbose_name_plural = 'AccountModels'
        ordering = ['name', 'gender', 'email', 'phone_number']

    def __str__(self):
        return f'{self.name} Is {self.role}'