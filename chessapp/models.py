from django.db import models

# Create your models here.

class Player(models.Model):
    username: models.CharField = models.CharField(max_length=50)
    pass

