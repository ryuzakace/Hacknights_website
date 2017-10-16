from django.db import models

from django.contrib import auth

class hacker(auth.models.User, auth.models.PermissionsMixin):

    def __str__(self):
        return self.username

# Create your models here.
