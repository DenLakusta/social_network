from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):

    username = models.CharField('username', max_length=150, unique=True)
    last_visit = models.DateTimeField(auto_now_add=True)


