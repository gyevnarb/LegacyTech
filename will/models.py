from django.db import models


class User(models.Model):
    first_names = models.CharField(max_length=256)
    last_names = models.CharField(max_length=512)
