from django.db import models
from django.contrib.auth.models import User
from uuid import uuid4

class EmailConfirm(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    token = models.CharField(default=uuid4, max_length=36)
