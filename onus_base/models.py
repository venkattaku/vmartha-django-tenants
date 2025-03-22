from django.contrib.auth.models import AbstractUser
from django.db import models
from hospitals.models import Hospital

class OnUsUser(AbstractUser):
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.username