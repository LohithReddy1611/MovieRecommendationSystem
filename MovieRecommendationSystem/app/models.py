# models.py

from django.db import models
from django.contrib.auth.hashers import check_password

class User(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100, default='')
    last_name = models.CharField(max_length=100, default='')
    username = models.CharField(max_length=100, unique=True, default='')
    password = models.CharField(max_length=100, default='')

    def login(self, password):
        return check_password(password, self.password)



