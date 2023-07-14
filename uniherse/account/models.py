from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    nickname = models.CharField(max_length=100)
    university = models.CharField(max_length=50)
    resident_registration_number = models.CharField(max_length=13, blank=True)

    def get_gender(self):
        seventh_digit = int(self.resident_registration_number[6])
        if seventh_digit == 2 or seventh_digit == 4:
            return '여자'
        else:
            return '남자'

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='customuser_set',
        blank=True
    )

    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='customuser_set',
        blank=True
    )
