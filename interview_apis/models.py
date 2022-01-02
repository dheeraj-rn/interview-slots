# import datetime

from django.db import models
# from django.utils import timezone

ALLOWED_USER_TYPES = [
    ('candidate', 'candidate'),
    ('interviewer', 'interviewer'),
]


class Users(models.Model):
    name = models.CharField(max_length=200)
    user_type = models.CharField(
        max_length=200, choices=ALLOWED_USER_TYPES, default='candidate')


class Slots(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    available_from = models.DateTimeField('available from')
    available_to = models.DateTimeField('available to')
